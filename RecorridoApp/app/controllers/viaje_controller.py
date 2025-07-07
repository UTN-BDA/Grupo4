from models.viaje import Viaje
from models.ruta import Ruta
from app import db

def buscar_viajes(origen, destino):
    # Buscar rutas que tengan ese origen y destino
    rutas = Ruta.query.filter_by(origen=origen, destino=destino).all()
    if not rutas:
        return []  # no hay rutas

    ruta_ids = [ruta.id for ruta in rutas]

    # Buscar viajes con esas rutas
    viajes = Viaje.query.filter(Viaje.ruta_id.in_(ruta_ids)).all()

    # Puedes devolver un listado serializado (por ejemplo con dataclasses o .__dict__)
    return [viaje.__dict__ for viaje in viajes]
