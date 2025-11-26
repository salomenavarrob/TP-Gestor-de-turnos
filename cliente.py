from registro import Registro
from utilidad import pedir_dni

class Cliente(Registro):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return f"DNI: {self.dni} - Nombre: {self.nombre} - Apellido: {self.apellido} "

    def registrar_cliente(lista_clientes):
        dni = pedir_dni("Ingrese el DNI del cliente (entre 7 y 8 números): ")
        # Verificar si el DNI ya está registrado en la lista de clientes.
        for c in lista_clientes:
            if c.dni == dni:
                print(f"Este cliente DNI: {dni} está registrado")
                return None
        # Solicitar datos del cliente.   
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        # Crear el objeto Cliente y agregarlo a la lista.
        cliente = Cliente(nombre=nombre, apellido=apellido, dni=str(dni))
        lista_clientes.append(cliente)
        print("Cliente registrado: " + str(cliente))
        return cliente