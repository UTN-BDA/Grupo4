from flask import Blueprint, request, jsonify
from controllers.parada_controller import (
    obtener_todas_paradas,
    obtener_parada_por_id,
    obtener_lineas_por_parada,
    obtener_horarios_por_parada
)

paradas_bp = Blueprint('paradas', __name__)

@paradas_bp.route('/paradas', methods=['GET'])
def get_paradas():
    """Endpoint para obtener todas las paradas (para mostrar en el mapa)"""
    try:
        paradas = obtener_todas_paradas()
        return jsonify({
            "success": True,
            "total": len(paradas),
            "data": paradas
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@paradas_bp.route('/paradas/<int:parada_id>', methods=['GET'])
def get_parada_por_id(parada_id):
    """Endpoint para obtener una parada específica por ID"""
    try:
        parada = obtener_parada_por_id(parada_id)
        if not parada:
            return jsonify({
                "success": False,
                "error": "Parada no encontrada"
            }), 404
        
        return jsonify({
            "success": True,
            "data": parada
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@paradas_bp.route('/paradas/<int:parada_id>/lineas', methods=['GET'])
def get_lineas_por_parada(parada_id):
    """Endpoint para obtener las líneas que pasan por una parada"""
    try:
        lineas = obtener_lineas_por_parada(parada_id)
        return jsonify({
            "success": True,
            "total": len(lineas),
            "data": lineas
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@paradas_bp.route('/paradas/<int:parada_id>/horarios', methods=['GET'])
def get_horarios_por_parada(parada_id):
    """Endpoint para obtener horarios y tiempos de llegada de una parada"""
    try:
        tipo_dia = request.args.get('tipo_dia')
        horarios = obtener_horarios_por_parada(parada_id, tipo_dia)
        
        return jsonify({
            "success": True,
            "total": len(horarios),
            "data": horarios
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
