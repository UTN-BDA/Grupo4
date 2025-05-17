from dataclasses import dataclass, field
from app import db

@dataclass
class Disponibilidad(db.Model):
    
    id: int = field(init=False)
    viaje_id: int = field(init=False)
    asientos_totales: int = field(init=False)
    asientos_disponibles: int = field(init=False)

    __tablename__ = "disponibilidad"
    id = db.Column(db.Integer, primary_key=True)
    viaje_id = db.Column(db.Integer, db.ForeignKey("viaje.id"), nullable=False)
    asientos_totales = db.Column(db.Integer, nullable=False)
    asientos_disponibles = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Disponibilidad(id={self.id}, viaje_id={self.viaje_id}, asientos_totales={self.asientos_totales}, asientos_disponibles={self.asientos_disponibles})>"