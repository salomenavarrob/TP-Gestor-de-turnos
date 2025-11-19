from gestor_turnos import GestorTurnos
from cliente import Cliente
from profesionales import Profesionales
from turno import Turno

def mostrar_menu():
        gestor = GestorTurnos()
        listaprofesionales = []
        listacliente = []
        print("**************")
        print('SISTEMA DE GESTIÓN DE TURNOS')
        print("**************")
        print("--------------------------------------")
        print("MENU PRINCIPAL")
        print("--------------------------------------")

        menu = """
            [1] Registrar nuevo Cliente
            [2] Registrar nuevo Empleado
            [3] Solicitar turno
            [4] Listar turnos existentes
            [5] Modificar turno
            [6] Cancelar turno
            [7] Guardar datos 
            [8] Salir
            """
        print(menu)

        while True:
            opcion = input("Seleccione la opción deseada (1 - 8): ")
            if opcion == "1":
                nombre = input ("Ingrese el nombre del cliente:")
                apellido = input ("Ingrese el apellido del cliente: ")
                dni = input ("Ingrese el dni del cliente:")
                cliente = Cliente (nombre=nombre, apellido=apellido, dni=dni)
            
                # if cliente.validar ():
                listacliente.append (cliente)
                print("Cliente registrado correctamente")
                # else:
                   # print ("Este cliente tiene un turno registrado")

            elif opcion == "2":
                nombre = input ("Ingrese el nombre del empleado:" )
                servicio = input ("Ingrese el servicio:" )
                profesionales = Profesionales (nombre= nombre, servicio= servicio)
                listaprofesionales.append (profesionales)
                print ("Profesional registrado")

            elif opcion == "3":
                if not cliente or not profesionales:
                    print ("Debe haber al menos un cliente y un empleado registrado")
                    continue 
                dni = input ("dni: ")
                profesional = input ("Profesional asignado: ")
                fecha = input ("fecha: ")
                hora = input ("hora: ")
                turno = Turno (cliente = dni, profesional= profesional, fecha= fecha, hora= hora)
                gestor.registrar_turno (turno)

            elif opcion == "4":
                gestor.listar_turnos()

            elif opcion == "5":
                dni = input ("Ingrese el dni del cliente:")
                nueva_fecha = input ("Nueva fecha: ")
                nueva_hora = input ("Nueva hora: ")
                gestor.modificar_turno(dni, nueva_fecha, nueva_hora)

            elif opcion == "6":
                dni = input ("dni:")
                fecha = input ("fecha")
                hora = input ("horario: ")
                gestor.cancelar_turno(dni, fecha, hora)

            elif opcion == "7":
                
                gestor.guardar_datos()

            elif opcion == "8":
                gestor.guardar_datos()
                print ("Saliendo del sistema")
                break

            else: 
                print ("Opcion invalida")


mostrar_menu()