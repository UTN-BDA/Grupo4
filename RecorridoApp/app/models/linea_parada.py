from dataclasses import dataclass, field
from app import db

@dataclass
class LineaParada(db.Model):

    id: int = field(init=False)
    linea_id: int = field(init=False)
    parada_id: int = field(init=False)
    orden: int = field(init=False)  # orden de la parada en la línea

    __tablename__ = "linea_parada"
    id = db.Column(db.Integer, primary_key=True)
    linea_id = db.Column(db.Integer, db.ForeignKey("linea.id"), nullable=False)
    parada_id = db.Column(db.Integer, db.ForeignKey("paradas.id"), nullable=False)
    orden = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<LineaParada(id={self.id}, linea_id={self.linea_id}, parada_id={self.parada_id}, orden={self.orden})>"