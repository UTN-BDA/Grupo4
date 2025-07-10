from app.models.viaje import Viaje
from app.models.ruta import Ruta
from app.models.empresa import Empresa
from app import db
from sqlalchemy import or_, and_

class ViajeService:
    
    @staticmethod
    def buscar_viajes(origen, destino):
        """Busca viajes de larga distancia entre origen y destino"""
        return db.session.query(Viaje, Ruta, Empresa)\
            .join(Ruta, Viaje.ruta_id == Ruta.id)\
            .join(Empresa, Viaje.empresa_id == Empresa.id)\
            .filter(
                or_(
                    and_(
                        Ruta.origen.ilike(f'%{origen}%'),
                        Ruta.destino.ilike(f'%{destino}%')
                    ),
                    and_(
                        Ruta.origen.ilike(f'%{destino}%'),
                        Ruta.destino.ilike(f'%{origen}%')
                    )
                )
            )\
            .order_by(Viaje.hora_salida)\
            .all()
    
    @staticmethod
    def obtener_todos_viajes():
        """Obtiene todos los viajes disponibles"""
        return db.session.query(Viaje, Ruta, Empresa)\
            .join(Ruta, Viaje.ruta_id == Ruta.id)\
            .join(Empresa, Viaje.empresa_id == Empresa.id)\
            .order_by(Viaje.hora_salida)\
            .all()
