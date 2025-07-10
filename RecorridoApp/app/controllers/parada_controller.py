from flask import Blueprint, jsonify, request
from app.services.parada_service import ParadaService
from app.schemas.parada_schema import ParadaSchema

parada_bp = Blueprint('paradas', __name__)

@parada_bp.route('/paradas', methods=['GET'])
def obtener_todas_paradas():
    """Endpoint para obtener todas las paradas (para mostrar en el mapa)"""
    try:
        paradas = ParadaService.obtener_todas_paradas()
        schema = ParadaSchema(many=True)
        return jsonify({
            'success': True,
            'data': schema.dump(paradas),
            'total': len(paradas)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@parada_bp.route('/paradas/<int:parada_id>', methods=['GET'])
def obtener_parada_por_id(parada_id):
    """Endpoint para obtener una parada específica"""
    try:
        parada = ParadaService.obtener_parada_por_id(parada_id)
        if not parada:
            return jsonify({
                'success': False,
                'error': 'Parada no encontrada'
            }), 404
        
        schema = ParadaSchema()
        return jsonify({
            'success': True,
            'data': schema.dump(parada)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@parada_bp.route('/paradas/<int:parada_id>/lineas', methods=['GET'])
def obtener_lineas_por_parada(parada_id):
    """Endpoint para obtener las líneas que pasan por una parada"""
    try:
        lineas_data = ParadaService.obtener_lineas_por_parada(parada_id)
        
        # Formatear la respuesta
        lineas = []
        for linea, empresa, orden in lineas_data:
            linea_dict = {
                'id': linea.id,
                'codigo': linea.codigo,
                'nombre': linea.nombre,
                'frecuencia': linea.frecuencia,
                'empresa': {
                    'id': empresa.id,
                    'nombre': empresa.nombre
                },
                'orden': orden
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

@parada_bp.route('/paradas/<int:parada_id>/horarios', methods=['GET'])
def obtener_horarios_por_parada(parada_id):
    """Endpoint para obtener horarios y tiempos de llegada de una parada"""
    try:
        tipo_dia = request.args.get('tipo_dia', None)
        horarios = ParadaService.obtener_horarios_por_parada(parada_id, tipo_dia)
        
        # Calcular próximas llegadas
        horarios_con_tiempo = ParadaService.calcular_proxima_llegada(horarios)
        
        # Formatear respuesta
        resultado = []
        for item in horarios_con_tiempo:
            horario_dict = {
                'id': item['horario'].id,
                'hora': item['horario'].hora.strftime('%H:%M'),
                'tipo_dia': item['horario'].tipo_dia,
                'proxima_llegada': item['proxima_llegada'],
                'linea': {
                    'id': item['linea'].id,
                    'codigo': item['linea'].codigo,
                    'nombre': item['linea'].nombre,
                    'frecuencia': item['linea'].frecuencia
                },
                'empresa': {
                    'id': item['empresa'].id,
                    'nombre': item['empresa'].nombre
                }
            }
            resultado.append(horario_dict)
        
        return jsonify({
            'success': True,
            'data': resultado,
            'total': len(resultado)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500