from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config


ma = Marshmallow()
db=SQLAlchemy()


def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)

    # Configuracion del contexto
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    # Inicializar extensiones
    ma.init_app(app)
    db.init_app(app)


    # Registrar blueprints
    #from app.resources import home
    #app.register_blueprint(home, url_prefix='/api/v1')
    

    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app

