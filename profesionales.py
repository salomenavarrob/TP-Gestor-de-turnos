from registro import Registro

class Profesionales (Registro):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def registrar_nuevo_empleado(self):
        nuevo = self.empleado.ingresar_valores()
        self.lista_empleados.append(nuevo)
        print("Empleado registrado correctamente")