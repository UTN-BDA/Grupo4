from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Empresa:
    id: int
    nombre: str