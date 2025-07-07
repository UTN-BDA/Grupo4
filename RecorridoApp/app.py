from app import create_app
import logging
from routes.viajes import viajes_bp

# Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Crear app Flask según el contexto de entorno
app = create_app()
app.app_context().push()
if __name__ == '__main__':
    """
    Server Startup
    """
    app.run(host="0.0.0.0", debug=False, port=5000)
    app.register_blueprint(viajes_bp)
    