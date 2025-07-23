from flask import Blueprint, request, jsonify
from controllers.linea_controller import (
    obtener_todas_lineas,
    obtener_linea_por_id,
    obtener_recorrido_linea,
    buscar_lineas_por_codigo
)

lineas_bp = Blueprint('lineas', __name__)

@lineas_bp.route('/lineas', methods=['GET'])
def get_lineas():
    """Endpoint para obtener todas las líneas o buscar por código"""
    codigo = request.args.get('codigo')
    
    if codigo:
        lineas = buscar_lineas_por_codigo(codigo)
    else:
        lineas = obtener_todas_lineas()
    
    return jsonify({
        "success": True,
        "total": len(lineas),
        "data": lineas
    })

@lineas_bp.route('/lineas/<int:linea_id>', methods=['GET'])
def get_linea_por_id(linea_id):
    """Endpoint para obtener una línea específica por ID"""
    try:
        linea = obtener_linea_por_id(linea_id)
        if not linea:
            return jsonify({
                "success": False,
                "error": "Línea no encontrada"
            }), 404
        
        return jsonify({
            "success": True,
            "data": linea
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@lineas_bp.route('/lineas/<int:linea_id>/recorrido', methods=['GET'])
def get_recorrido_linea(linea_id):
    """Endpoint para obtener el recorrido completo de una línea"""
    try:
        recorrido = obtener_recorrido_linea(linea_id)
        
        return jsonify({
            "success": True,
            "data": recorrido
        })
    except ValueError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
