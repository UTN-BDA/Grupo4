from dataclasses import dataclass, field
from app import db

@dataclass
class Empresa(db.Model):

    id: int = field(init=False)
    nombre: str = field(init=False)

    __tablename__ = "empresa"
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Empresa(id={self.id}, nombre='{self.nombre}')>"