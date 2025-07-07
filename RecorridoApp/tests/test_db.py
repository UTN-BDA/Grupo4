import sys
import os

# Agregamos la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.ruta import Ruta

# Crear una instancia de la app
app = create_app()

def test_conexion():
    with app.app_context():  # ✅ Creamos el application context
        try:
            rutas = Ruta.query.all()
            print(f"✔ Conexión exitosa. Se encontraron {len(rutas)} rutas.")
        except Exception as e:
            print("✖ Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    test_conexion()
