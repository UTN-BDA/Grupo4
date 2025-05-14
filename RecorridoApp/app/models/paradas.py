from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Paradas:
    id: int
    ubicacion: str
    lat: int
    long: int
