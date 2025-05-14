from dataclasses import dataclass
from datetime import time
from pasaje import Pasaje
from empresa import Empresa

@dataclass(init=False, repr=True, eq=True)
class Viajes:
    id: int
    pasaje_id: Pasaje
    destino: str
    horario: time
    empresa_id: Empresa
    costo_unitario: int
    tiempo_llegada: time

def validar_id(id_pasaje, id_empresa, pasajes, empresas):
    if id_pasaje not in [Pasaje.id for Pasaje in pasajes]:
        raise ValueError("ID de pasaje no valido")
    if id_empresa not in [Empresa.id for Empresa in empresas]:
        raise ValueError("ID de linea no valido")
