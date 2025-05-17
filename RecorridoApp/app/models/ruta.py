from dataclasses import dataclass, field
from app import db
@dataclass
class Ruta(db.Model):

    id: int = field(init=False)
    origen: str = field(init=False)
    destino: str = field(init=False)
    distancia_km: float = field(init=False)
    tiempo_estimado: int = field(init=False)

    __tablename__ = "ruta"
    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    distancia_km = db.Column(db.Float, nullable=False)
    tiempo_estimado = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Ruta(id={self.id}, origen='{self.origen}', destino='{self.destino}', distancia_km={self.distancia_km}, tiempo_estimado={self.tiempo_estimado})>"
