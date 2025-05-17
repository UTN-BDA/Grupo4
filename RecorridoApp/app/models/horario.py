from dataclasses import dataclass, field
from app import db
from datetime import time

@dataclass
class Horario(db.Model):
    
    id: int = field(init=False)
    linea_parada: int = field(init=False)
    hora: time = field(init=False)
    tipo_dia: str = field(init=False)
    
    __tablename__ = "horario"
    id= db.Column(db.Integer, primary_key=True)
    linea_parada = db.Column(db.Integer, db.ForeignKey("linea_parada.id"), nullable=False)
    hora = db.Column(db.Time, nullable=False)
    tipo_dia = db.Column(db.String(10), nullable=False)  # 'laboral', 'fin_de_semana', 'feriado'
    
    def __repr__(self):
        return f"<Horario(id={self.id}, linea_parada={self.linea_parada}, hora='{self.hora}', tipo_dia='{self.tipo_dia}')>"