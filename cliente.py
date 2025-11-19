from registro import Registro

class Cliente (Registro):

    clientes = []

    def __init__(self, **kwargs):
     super().__init__(**kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni}"
  
    def registrar_cliente(self):
        nombre = input ("nombre:")
        apellido = input ("apellido: ")
        dni = input ("dni:")
        cliente = Cliente (nombre, apellido, dni)
        validacion = cliente.validar (cliente)
        if validacion == False:
            self.clientes.append (cliente)
            print("Cliente registrado correctamente")
            return cliente
        else:
            print ("Este cliente tiene un turno registrado")

    def validar (self, cliente):
        if cliente.dni in self.clientes:
            return True
        else:
            return False 