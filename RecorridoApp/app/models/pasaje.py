from dataclasses import dataclass
from datetime import datetime
@dataclass(init=False, repr=True, eq=True)

class Pasaje:
    id: int
    destino: str
    salida: str
    fecha_salida: datetime
    fecha_llegada: datetime
    unidades: int   #n° pasajes
