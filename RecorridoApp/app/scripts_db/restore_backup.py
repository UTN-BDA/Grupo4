import subprocess
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD") 
DB_NAME = os.getenv("POSTGRES_DB")
DB_CONTAINER = "recorrido-postgresql"

def restore_backup(backup_file_path):
    """
    Restaura la base de datos de colectivos desde un archivo de backup
    """
    if not os.path.exists(backup_file_path):
        print(f"Archivo de backup no encontrado: {backup_file_path}")
        return False

    print(f"Iniciando restauración de la base de datos '{DB_NAME}'...")
    print(f"Desde archivo: {backup_file_path}")
    print(f"Contenedor: {DB_CONTAINER}")
    
    # Confirmar la operación (esto borrará datos existentes)
    confirm = input("ADVERTENCIA: Esto eliminará todos los datos actuales de la base. ¿Continuar? (s/n): ")
    if confirm.lower() not in ['s', 'si', 'yes', 'y']:
        print("Operación cancelada.")
        return False

    try:
        # pg_restore: comando de PostgreSQL para restaurar backups
        with open(backup_file_path, "rb") as f:
            subprocess.run([
                "docker", "exec", "-i",  # -i: modo interactivo (lee desde stdin)
                "-e", f"PGPASSWORD={DB_PASSWORD}",  # Variable de entorno para password
                DB_CONTAINER,
                "pg_restore",
                "--no-owner",      # No restaurar información de propietario (evita errores)
                "--no-privileges", # No restaurar privilegios (evita errores)
                "-U", DB_USER,     # Usuario de PostgreSQL
                "-d", DB_NAME,     # Base de datos destino
                # "-c",              # Clean: eliminar objetos existentes antes de crear
                "-v"               # Verbose: mostrar detalles del proceso
            ], stdin=f, check=True)  # stdin=f: pasar el archivo como entrada

        print("Restauración completada con éxito.")
        print("La base de datos de colectivos ha sido restaurada.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error durante la restauración: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

def list_available_backups():
    """Lista los backups disponibles en el directorio"""
    backup_dir = "./backups"
    if not os.path.exists(backup_dir):
        print("No existe el directorio de backups")
        return []
    
    backups = [f for f in os.listdir(backup_dir) if f.endswith('.backup')]
    if backups:
        print("Backups disponibles:")
        for i, backup in enumerate(sorted(backups, reverse=True), 1):
            full_path = os.path.join(backup_dir, backup)
            size_kb = os.path.getsize(full_path) / 1024
            print(f"  {i}. {backup} ({size_kb:.2f} KB)")
    else:
        print("No hay backups disponibles")
    
    return backups

if __name__ == "__main__":
    # Mostrar backups disponibles y permitir selección interactiva
    backups = list_available_backups()
    if backups:
        try:
            choice = input("\nIngresa el número del backup a restaurar (o 'q' para salir): ")
            if choice.lower() == 'q':
                exit()
            
            index = int(choice) - 1
            if 0 <= index < len(backups):
                selected_backup = f"./backups/{sorted(backups, reverse=True)[index]}"
                restore_backup(selected_backup)
            else:
                print("Número inválido")
        except (ValueError, KeyboardInterrupt):
            print("Operación cancelada")
    else:
        print("No hay backups disponibles. Ejecuta primero backup.py")