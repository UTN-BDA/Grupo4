from dataclasses import dataclass, field
from app import db

@dataclass
class Linea(db.Model):

    id: int = field(init=False)
    codigo: str = field(init=False)
    nombre: str = field(init=False)
    empresa_id: str = field(init=False)
    frecuencia: int = field(init=False)

    __tablename__ = "linea"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresa.id"), nullable=False)
    frecuencia = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Linea(id={self.id}, codigo='{self.codigo}', nombre='{self.nombre}', tipo='{self.tipo}', frecuencia={self.frecuencia})>" 