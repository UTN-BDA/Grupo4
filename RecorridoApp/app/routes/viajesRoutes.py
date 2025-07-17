from flask import Blueprint, request, jsonify
from controllers.viaje_controller import buscar_viajes

viajes_bp = Blueprint('viajes', __name__)

@viajes_bp.route('/viajes', methods=['GET'])
def obtener_viajes():
    origen = request.args.get('origen')
    destino = request.args.get('destino')

    if not origen or not destino:
        return jsonify({"error": "Debe especificar origen y destino"}), 400

    viajes = buscar_viajes(origen, destino)
    return jsonify({
    "success": True,
    "total": len(viajes),
    "data": viajes
})

