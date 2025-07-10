from app.models.linea import Linea
from app.models.paradas import Parada
from app.models.linea_parada import LineaParada
from app.models.empresa import Empresa
from app import db

class LineaService:
    
    @staticmethod
    def obtener_todas_lineas():
        """Obtiene todas las líneas con información de empresa"""
        return db.session.query(Linea, Empresa)\
            .join(Empresa, Linea.empresa_id == Empresa.id)\
            .order_by(Linea.codigo)\
            .all()
    
    @staticmethod
    def obtener_linea_por_id(linea_id):
        """Obtiene una línea específica por ID"""
        return db.session.query(Linea, Empresa)\
            .join(Empresa, Linea.empresa_id == Empresa.id)\
            .filter(Linea.id == linea_id)\
            .first()
    
    @staticmethod
    def obtener_recorrido_linea(linea_id):
        """Obtiene el recorrido completo de una línea (paradas en orden)"""
        return db.session.query(Parada, LineaParada.orden)\
            .join(LineaParada, Parada.id == LineaParada.parada_id)\
            .filter(LineaParada.linea_id == linea_id)\
            .order_by(LineaParada.orden)\
            .all()
    
    @staticmethod
    def buscar_lineas_por_codigo(codigo):
        """Busca líneas por código"""
        return db.session.query(Linea, Empresa)\
            .join(Empresa, Linea.empresa_id == Empresa.id)\
            .filter(Linea.codigo.ilike(f'%{codigo}%'))\
            .all()