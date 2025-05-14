from dataclasses import dataclass
from datetime import time, datetime
from typing import Union
from pasaje import Pasaje
from paradas import Paradas
from linea import Linea

@dataclass(False, repr=True, eq=True)
class Horario:
    id: int
    id_linea: Linea
    id_parada: Paradas
    if Pasaje != "":
        horario: Union[datetime, time]
    else:
        horario: time
    orden: int

def validar_id(id_linea, id_parada, lineas, paradas):
    if id_linea not in [Linea.id for Linea in lineas]:
        raise ValueError("ID de linea no valido")
    if id_parada not in [Paradas.id for Paradas in paradas]:
        raise ValueError("ID de parada no valido")
