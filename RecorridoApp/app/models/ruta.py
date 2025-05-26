from dataclasses import dataclass, field
from app import db

@dataclass
class Ruta(db.Model):

    id: int = field(init=False)
    origen: str = field(init=False)
    destino: str = field(init=False)

    __tablename__ = "ruta"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f"Ruta(id={self.id}, origen='{self.origen}', destino='{self.destino}')"
