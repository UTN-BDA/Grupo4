from flask import Blueprint, jsonify, request
from app.services.linea_service import LineaService
from app.schemas.linea_schema import LineaSchema, LineaConRecorridoSchema

linea_bp = Blueprint('lineas', __name__)

@linea_bp.route('/lineas', methods=['GET'])
def obtener_todas_lineas():
    """Endpoint para obtener todas las líneas"""
    try:
        codigo = request.args.get('codigo', None)
        
        if codigo:
            lineas_data = LineaService.buscar_lineas_por_codigo(codigo)
        else:
            lineas_data = LineaService.obtener_todas_lineas()
        
        # Formatear respuesta
        lineas = []
        for linea, empresa in lineas_data:
            linea_dict = {
                'id': linea.id,
                'codigo': linea.codigo,
                'nombre': linea.nombre,
                'frecuencia': linea.frecuencia,
                'empresa': {
                    'id': empresa.id,
                    'nombre': empresa.nombre
                }
            }
            lineas.append(linea_dict)
        
        return jsonify({
            'success': True,
            'data': lineas,
            'total': len(lineas)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@linea_bp.route('/lineas/<int:linea_id>', methods=['GET'])
def obtener_linea_por_id(linea_id):
    """Endpoint para obtener una línea específica"""
    try:
        linea_data = LineaService.obtener_linea_por_id(linea_id)
        if not linea_data:
            return jsonify({
                'success': False,
                'error': 'Línea no encontrada'
            }), 404
        
        linea, empresa = linea_data
        linea_dict = {
            'id': linea.id,
            'codigo': linea.codigo,
            'nombre': linea.nombre,
            'frecuencia': linea.frecuencia,
            'empresa': {
                'id': empresa.id,
                'nombre': empresa.nombre
            }
        }
        
        return jsonify({
            'success': True,
            'data': linea_dict
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@linea_bp.route('/lineas/<int:linea_id>/recorrido', methods=['GET'])
def obtener_recorrido_linea(linea_id):
    """Endpoint para obtener el recorrido completo de una línea"""
    try:
        # Obtener información de la línea
        linea_data = LineaService.obtener_linea_por_id(linea_id)
        if not linea_data:
            return jsonify({
                'success': False,
                'error': 'Línea no encontrada'
            }), 404
        
        linea, empresa = linea_data
        
        # Obtener recorrido
        recorrido_data = LineaService.obtener_recorrido_linea(linea_id)
        
        # Formatear recorrido
        recorrido = []
        for parada, orden in recorrido_data:
            parada_dict = {
                'id': parada.id,
                'ubicacion': parada.ubicacion,
                'latitud': parada.latitud,
                'longitud': parada.longitud,
                'detalles_referencia': parada.detalles_referencia,
                'orden': orden
            }
            recorrido.append(parada_dict)
        
        resultado = {
            'linea': {
                'id': linea.id,
                'codigo': linea.codigo,
                'nombre': linea.nombre,
                'frecuencia': linea.frecuencia,
                'empresa': {
                    'id': empresa.id,
                    'nombre': empresa.nombre
                }
            },
            'recorrido': recorrido,
            'total_paradas': len(recorrido)
        }
        
        return jsonify({
            'success': True,
            'data': resultado
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500