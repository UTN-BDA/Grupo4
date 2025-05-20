from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.config import config
from app.Routes.main import bp as main_bp

ma = Marshmallow()
db=SQLAlchemy()
migrate = Migrate()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)

    # Configuracion del contexto
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    # Inicializar extensiones
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


    # Registrar blueprints
    #from app.resources import home
    #app.register_blueprint(home, url_prefix='/api/v1')
    

    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    app.register_blueprint(main_bp)
    return app
