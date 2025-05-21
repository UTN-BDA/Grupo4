from dataclasses import dataclass, field
from app import db
from datetime import datetime

@dataclass
class Ruta(db.Model):

    id: int = field(init=False)
    origen: str = field(init=False)
    destino: str = field(init=False)
    fecha_salida: datetime 
    fecha_llegada: datetime

    __tablename__ = "ruta"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=False)
    fecha_llegada = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Ruta(id={self.id}, origen='{self.origen}', destino='{self.destino}', hora_salida='{self.hora_salida}', hora_llegada='{self.hora_llegada}')"
