from dataclasses import dataclass, field
from app import db

@dataclass
class Viaje(db.Model):

    id: int = field(init=False)
    ruta_id: int = field(init=False)
    empresa_id: int = field(init=False)
    costo_base: float = field(init=False)

    __tablename__ = "viaje"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ruta_id = db.Column(db.Integer, db.ForeignKey("ruta.id"), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresa.id"), nullable=False)
    costo_base = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Viaje(id={self.id}, ruta_id={self.ruta_id}, empresa_id={self.empresa_id}, fecha_salida='{self.fecha_salida}', fecha_llegada='{self.fecha_llegada}', costo_base={self.costo_base})>"