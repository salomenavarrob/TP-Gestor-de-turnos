from cliente import Cliente
from registro import Registro

class Turno (Registro):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

def coincide (self, turno):
    if self.empleado == turno.empleado and self.fecha == turno.fecha and self.hora == turno.hora: 
        return True
    return False  