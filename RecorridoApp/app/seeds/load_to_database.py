"""
Script para cargar datos desde un archivo JSON a la base de datos PostgreSQL
"""

import json
import os
from datetime import time
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def parse_time(time_str):
    """Convierte un string de hora (HH:MM) a un objeto time"""
    try:
        return time(*map(int, time_str.split(':')))
    except ValueError:
        print(f"Error al parsear hora: {time_str}")
        return None

def get_db_connection():
    """Establece conexión con la base de datos PostgreSQL en Docker usando variables de entorno"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Conexión a la base de datos establecida")
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

def load_json_data(file_path):
    """Lee el archivo JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"JSON cargado desde: {file_path}")
        return data
    except Exception as e:
        print(f"Error al cargar JSON: {e}")
        raise

def insert_data(conn, data):
    """Inserta los datos del JSON en la base de datos"""
    try:
        cursor = conn.cursor()

        # 1. Insertar empresas y mapear nombres a IDs
        empresa_map = {}
        for empresa in data["empresas"]:
            cursor.execute(
                "INSERT INTO empresa (nombre) VALUES (%s) RETURNING id",
                (empresa["nombre"],)
            )
            empresa_id = cursor.fetchone()[0]
            empresa_map[empresa["nombre"]] = empresa_id
        print(f"Insertadas {len(data['empresas'])} empresas")

        # 2. Insertar paradas y mapear ubicaciones a IDs
        parada_map = {}
        for parada in data["paradas"]:
            cursor.execute(
                """
                INSERT INTO paradas (ubicacion, latitud, longitud, detalles_referencia)
                VALUES (%s, %s, %s, %s) RETURNING id
                """,
                (parada["ubicacion"], parada["latitud"], parada["longitud"], parada["detalles_referencia"])
            )
            parada_id = cursor.fetchone()[0]
            parada_map[parada["ubicacion"]] = parada_id
        print(f"Insertadas {len(data['paradas'])} paradas")

        # 3. Insertar líneas y mapear códigos a IDs
        linea_map = {}
        for linea in data["lineas"]:
            cursor.execute(
                """
                INSERT INTO linea (codigo, nombre, empresa_id, frecuencia)
                VALUES (%s, %s, %s, %s) RETURNING id
                """,
                (linea["codigo"], linea["nombre"], empresa_map[linea["empresa"]], linea["frecuencia"])
            )
            linea_id = cursor.fetchone()[0]
            linea_map[linea["codigo"]] = linea_id
        print(f"Insertadas {len(data['lineas'])} líneas")

        # 4. Insertar relaciones línea-parada
        linea_parada_map = {}
        for lp in data["linea_paradas"]:
            cursor.execute(
                """
                INSERT INTO linea_parada (id, linea_id, parada_id, orden)
                VALUES (%s, %s, %s, %s) RETURNING id
                """,
                (lp["id"], linea_map[lp["linea_codigo"]], parada_map[lp["parada_ubicacion"]], lp["orden"])
            )
            linea_parada_id = cursor.fetchone()[0]
            linea_parada_map[lp["id"]] = linea_parada_id
        print(f"Insertadas {len(data['linea_paradas'])} relaciones línea-parada")

        # 5. Insertar horarios
        for horario in data["horarios"]:
            hora = parse_time(horario["hora"])
            if hora:
                cursor.execute(
                    """
                    INSERT INTO horario (id, linea_parada, hora, tipo_dia)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (horario["id"], linea_parada_map[horario["linea_parada_id"]], hora, horario["tipo_dia"])
                )
        print(f"Insertados {len(data['horarios'])} horarios")

        # 6. Insertar rutas
        for ruta in data["rutas"]:
            cursor.execute(
                """
                INSERT INTO ruta (id, origen, destino)
                VALUES (%s, %s, %s)
                """,
                (ruta["id"], ruta["origen"], ruta["destino"])
            )
        print(f"Insertadas {len(data['rutas'])} rutas")

        # 7. Insertar viajes
        for viaje in data["viajes"]:
            hora_salida = parse_time(viaje["hora_salida"])
            hora_llegada = parse_time(viaje["hora_llegada"])
            if hora_salida and hora_llegada:
                cursor.execute(
                    """
                    INSERT INTO viaje (id, ruta_id, empresa_id, hora_salida, hora_llegada, costo_base)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (viaje["id"], viaje["ruta_id"], empresa_map[viaje["empresa"]], hora_salida, hora_llegada, viaje["costo_base"])
                )
        print(f"Insertados {len(data['viajes'])} viajes")

        # Confirmar transacción
        conn.commit()
        print("Todos los datos insertados correctamente")

    except psycopg2.Error as e:
        print(f"Error al insertar datos: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()

def main():
    """Función principal para cargar los datos"""
    try:
        # Ruta al archivo JSON
        json_file = os.path.join(os.path.dirname(__file__), "datos_transporte_completo.json")
        
        # Cargar datos JSON
        data = load_json_data(json_file)
        
        # Conectar a la base de datos
        conn = get_db_connection()
        
        # Insertar datos
        insert_data(conn, data)
        
        # Mostrar estadísticas
        print("\n ESTADÍSTICAS DE CARGA:")
        print(f"   Empresas: {len(data['empresas'])}")
        print(f"   Paradas: {len(data['paradas'])}")
        print(f"   Líneas: {len(data['lineas'])}")
        print(f"   Relaciones Línea-Parada: {len(data['linea_paradas'])}")
        print(f"   Horarios: {len(data['horarios'])}")
        print(f"   Rutas: {len(data['rutas'])}")
        print(f"   Viajes: {len(data['viajes'])}")
        
    except Exception as e:
        print(f"Error en el proceso de carga: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Conexión a la base de datos cerrada")

if __name__ == "__main__":
    main()