from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from app.config import config

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)

    # Configurar CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "exp://192.168.1.100:8081"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Configuracion del contexto
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    # Inicializar extensiones
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos
    from .models.empresa import Empresa
    from .models.linea import Linea
    from .models.paradas import Parada
    from .models.linea_parada import LineaParada
    from .models.horario import Horario
    from .models.ruta import Ruta
    from .models.viaje import Viaje

    # Registrar blueprints
    from app.controllers import viaje_bp
    from app.controllers import linea_bp
    from app.controllers import parada_bp

    app.register_blueprint(viaje_bp, url_prefix='/api/v1')
    app.register_blueprint(linea_bp, url_prefix='/api/v1')
    app.register_blueprint(parada_bp, url_prefix='/api/v1')

    # Ruta de salud de la API
    @app.route('/api/v1/health')
    def health_check():
        return {'status': 'OK', 'message': 'API funcionando correctamente'}

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
