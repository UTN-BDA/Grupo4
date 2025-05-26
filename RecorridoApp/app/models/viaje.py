from dataclasses import dataclass, field
from app import db
import datetime

@dataclass
class Viaje(db.Model):

    id: int = field(init=False)
    ruta_id: int = field(init=False)
    empresa_id: int = field(init=False)
    hora_salida: datetime.time
    hora_llegada: datetime.time
    costo_base: float = field(init=False)

    __tablename__ = "viaje"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ruta_id = db.Column(db.Integer, db.ForeignKey("ruta.id"), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresa.id"), nullable=False)
    hora_salida = db.Column(db.Time, nullable=False)
    hora_llegada = db.Column(db.Time, nullable=False)
    costo_base = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Viaje(id={self.id}, ruta_id={self.ruta_id}, empresa_id={self.empresa_id}, hora_salida='{self.hora_salida}', hora_llegada='{self.hora_llegada}', costo_base={self.costo_base})>"