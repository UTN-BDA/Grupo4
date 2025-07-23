import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_CONTAINER = "recorrido-postgresql"
BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")

# Generar nombre del archivo con timestamp
FILENAME = f"{DB_NAME}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"
OUTPUT_PATH = os.path.join(BACKUP_DIR, FILENAME)

def create_backup():
    """
    Crea un backup de la base de datos 
    """
    # Crear directorio de backups si no existe
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Directorio de backups creado: {BACKUP_DIR}")

    print(f"Iniciando backup de la base de datos '{DB_NAME}'...")
    print(f"Contenedor: {DB_CONTAINER}")

    try:
        # pg_dump: comando de PostgreSQL para crear backups
        subprocess.run([
            "docker", "exec",  # Ejecutar comando dentro del contenedor
            "-e", f"PGPASSWORD={DB_PASSWORD}",  # Variable de entorno para password
            DB_CONTAINER,  # Nombre del contenedor
            "pg_dump",     # Comando de PostgreSQL para backup
            "-U", DB_USER, # Usuario de PostgreSQL
            "-F", "c",     # Formato custom (comprimido, más rápido que SQL plano)
            "-v",          # Verbose: mostrar progreso
            DB_NAME,       # Nombre de la base de datos
        ], check=True, stdout=open(OUTPUT_PATH, "wb"))  # Guardar salida en archivo binario

        print(f"Backup creado exitosamente en: {OUTPUT_PATH}")
        print(f"Tamaño del archivo: {os.path.getsize(OUTPUT_PATH) / 1024:.2f} KB")
        
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el backup: {e}")
        # Eliminar archivo parcial si existe
        if os.path.exists(OUTPUT_PATH):
            os.remove(OUTPUT_PATH)
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    create_backup()