from dataclasses import dataclass, field
from app import db
@dataclass
class Ruta(db.Model):

    id: int = field(init=False)
    origen: str = field(init=False)
    destino: str = field(init=False)
    hora_salida: str = field(init=False)
    hora_llegada: str = field(init=False)   

    __tablename__ = "ruta"
    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    hora_llegada = db.Column(db.String(100), nullable=False)
    hora_salida = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Ruta(id={self.id}, origen='{self.origen}', destino='{self.destino}', hora_salida='{self.hora_salida}', hora_llegada='{self.hora_llegada}')"
