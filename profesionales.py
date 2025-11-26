from registro import Registro
from utilidad import pedir_dni

class Profesionales (Registro):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return f"DNI: {self.dni} - Nombre: {self.nombre} - Servicio: {self.servicio} "
    
    def registrar_profesional(lista_profesionales):
        # Pedir DNI y verificar si ya está registrado con la lista.
        dni = pedir_dni("Ingrese el DNI del profesional (entre 7 y 8 números): ")
        for p in lista_profesionales:
            if p.dni == str(dni):
                print(f"Este profesional DNI: {dni} está registrado")
                return None
        # Solicitar datos del profesional.
        nombre = input("Ingrese el nombre del profesional: ")
        servicio = input("Ingrese el servicio: ")
        profesional = Profesionales(nombre=nombre, servicio=servicio, dni=str(dni))
        # Agregar el nuevo profesional a la lista.
        lista_profesionales.append(profesional)
        print("Profesional registrado: " + str(profesional))
        return profesional

