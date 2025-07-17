from flask import Blueprint, jsonify, request
from app.services.viaje_service import ViajeService

viaje_bp = Blueprint('viajes', __name__)

def formatear_viajes(viajes_data):
    """Función auxiliar para formatear un viaje"""
    viajes = []
    for viaje, ruta, empresa in viajes_data:
        viaje_dict = {
            'id': viaje.id,
            'hora_salida': viaje.hora_salida.strftime('%H:%M'),
            'hora_llegada': viaje.hora_llegada.strftime('%H:%M'),
            'costo_base': viaje.costo_base,
            'ruta': {
                'id': ruta.id,
                'origen': ruta.origen,
                'destino': ruta.destino
                },
            'empresa': {
                'id': empresa.id,
                'nombre': empresa.nombre
                }
            }
        viajes.append(viaje_dict)
    return viajes

@viaje_bp.route('/viajes', methods=['GET'])
def obtener_viajes():
    """Endpoint para obtener todos los viajes o buscar por origen/destino"""
    try:
        origen = request.args.get('origen', None)
        destino = request.args.get('destino', None)
        
        if origen and destino:
            viajes_data = ViajeService.buscar_viajes(origen, destino)
        else:
            viajes_data = ViajeService.obtener_todos_viajes()
        
        # Formatear respuesta
        viajes= formatear_viajes(viajes_data)

        return jsonify({
            'success': True,
            'data': viajes,
            'total': len(viajes)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@viaje_bp.route('/viajes/buscar', methods=['GET'])
def buscar_viajes():
    """Endpoint específico para buscar viajes por origen y destino"""
    try:
        origen = request.args.get('origen', '')
        destino = request.args.get('destino', '')
        
        if not origen or not destino:
            return jsonify({
                'success': False,
                'error': 'Origen y destino son requeridos'
            }), 400
        
        viajes_data = ViajeService.buscar_viajes(origen, destino)
        print(f"Origen: {origen}, Destino: {destino}")
        
        # Formatear respuesta
        viajes= formatear_viajes(viajes_data)
        
        return jsonify({
            'success': True,
            'data': viajes,
            'total': len(viajes),
            'busqueda': {
                'origen': origen,
                'destino': destino
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
