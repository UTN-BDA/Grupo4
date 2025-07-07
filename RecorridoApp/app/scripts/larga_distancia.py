import os
import csv
import json
import random
from datetime import datetime, timedelta
import logging

# --- Configuración y Datos Iniciales ---

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

EMPRESAS = [
    {"nombre": "Iselin"},
    {"nombre": "Andesmar"},
    {"nombre": "20 de Junio"},
    {"nombre": "A. Buttini"},
    {"nombre": "Cata"},
    {"nombre": "Chevallier"},
]

ORIGEN_PRINCIPAL = "San Rafael"

def leer_destinos_desde_csv(nombre_archivo):
    """Lee los destinos desde un archivo CSV."""
    destinos = []
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile, delimiter=';')
            for fila in lector:
                nombre = fila.get('nombre')
                tiempo = fila.get('tiempo_estimado')
                if nombre and tiempo:
                    destinos.append({
                        'nombre': nombre.strip(),
                        'tiempo_estimado': tiempo.strip()
                    })
                else:
                    logger.warning(f"Saltando fila de CSV incompleta: {fila}")
    except FileNotFoundError:
        logger.error(f"Error: No se encontró el archivo CSV en {nombre_archivo}")
        return None
    except Exception as e:
        logger.error(f"Error al leer el CSV: {e}")
        return None
    return destinos

def parse_tiempo(tstr):
    """Convierte una cadena 'HH:MM' a un objeto timedelta."""
    try:
        horas, minutos = map(int, tstr.split(':'))
        return timedelta(hours=horas, minutes=minutos)
    except ValueError:
        logger.error(f"Formato de tiempo inválido: {tstr}. Se usará 00:00.")
        return timedelta()

def generar_datos_viajes(empresas, destinos, origen_principal):
    """Genera una lista de viajes de ida y vuelta."""
    viajes = []
    rutas_set = set()

    for empresa in empresas:
        for dest in destinos:
            for _ in range(5): # Generar 5 viajes por cada ruta/empresa
                hora_salida = datetime(2025, 1, 1, random.randint(0, 23), random.choice(range(0, 56, 5)))
                tmp_estimado = parse_tiempo(dest["tiempo_estimado"])
                hora_llegada = hora_salida + tmp_estimado
                costo_aleatorio = random.randint(10000, 30000)

                # Viaje de Ida
                viajes.append({
                    "empresa": empresa["nombre"],
                    "origen": origen_principal,
                    "destino": dest["nombre"],
                    "hora_salida": hora_salida.strftime("%H:%M"),
                    "hora_llegada": hora_llegada.strftime("%H:%M"),
                    "costo_base": costo_aleatorio,
                })
                rutas_set.add((origen_principal, dest["nombre"]))

                # Viaje de Vuelta
                hora_salida_vuelta = hora_llegada + timedelta(hours=2) # Sale 2hs despues de llegar
                hora_llegada_vuelta = hora_salida_vuelta + tmp_estimado
                viajes.append({
                    "empresa": empresa["nombre"],
                    "origen": dest["nombre"],
                    "destino": origen_principal,
                    "hora_salida": hora_salida_vuelta.strftime("%H:%M"),
                    "hora_llegada": hora_llegada_vuelta.strftime("%H:%M"),
                    "costo_base": costo_aleatorio,
                })
                rutas_set.add((dest["nombre"], origen_principal))

    # Convertir el set de rutas a una lista de diccionarios
    rutas = [{"origen": o, "destino": d} for o, d in sorted(list(rutas_set))]
    return viajes, rutas


# --- Ejecución Principal ---

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    csv_path = os.path.join(script_dir, 'docs', 'data.csv')

    destinos_data = leer_destinos_desde_csv(csv_path)

    if destinos_data:
        viajes_generados, rutas_generadas = generar_datos_viajes(EMPRESAS, destinos_data, ORIGEN_PRINCIPAL)

        # Estructura de datos final a exportar
        datos_completos = {
            "empresas": EMPRESAS,
            "rutas": rutas_generadas,
            "viajes": viajes_generados
        }

        # Convertir a JSON y mostrar en consola
        # Para guardarlo en un archivo, ejecuta en la terminal:
        # python extractor.py > datos_viajes.json
        print(json.dumps(datos_completos, indent=4, ensure_ascii=False))

        logger.info(f"Se generaron {len(EMPRESAS)} empresas, {len(rutas_generadas)} rutas y {len(viajes_generados)} viajes.")