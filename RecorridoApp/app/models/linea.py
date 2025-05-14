from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Linea():
    id: int
    codigo: str
    nombre: str
    tipo: str
    frecuencia: int
