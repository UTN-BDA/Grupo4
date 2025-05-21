from dataclasses import dataclass, field
from app import db

@dataclass
class Parada(db.Model):

    id: int = field(init=False)
    ubicacion: str = field(init=False)
    latitud: float = field(init=False)
    longitud: float = field(init=False)
    detalles_referencia: str = field(init=False)

    __tablename__ = "paradas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ubicacion = db.Column(db.String(100), nullable=False, unique=True)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    detalles_referencia = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Parada(id={self.id}, ubicacion='{self.ubicacion}', lat={self.latitud}, long={self.longitud}, detalles_referencia='{self.detalles_referencia}')>"