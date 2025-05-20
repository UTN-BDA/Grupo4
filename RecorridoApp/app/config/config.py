from dotenv import load_dotenv
from pathlib import Path
import os

# Cargar variables de entorno desde el .env
basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')== 'True'
    SQLALCHEMY_RECORD_QUERIES = os.getenv('SQLALCHEMY_RECORD_QUERIES')== 'True'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    uri = os.getenv('DEV_DATABASE_URI')
    if not uri:
        raise ValueError("DEV_DATABASE_URI no está definida en el .env")
    SQLALCHEMY_DATABASE_URI = uri
    

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'testing': TestConfig,
        'production': ProductionConfig
    }

    return configuration[app]
