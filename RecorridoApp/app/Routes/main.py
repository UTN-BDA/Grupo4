from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return "Hola desde el blueprint"
