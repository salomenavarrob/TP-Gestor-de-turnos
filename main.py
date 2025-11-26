from gestor_turnos import GestorTurnos
from cliente import Cliente
from profesionales import Profesionales
from turno import Turno

def mostrar_menu():
        #Crear instancia de la clase GestorTurnos y lleno la lista de turnos con el csv.
        gestor = GestorTurnos()
        
        #Crear listas de profesionales y clientes de ejemplo.
        listaprofesionales = [Profesionales (nombre= "Alma", servicio= "tintura", dni = "22222222"), 
                              Profesionales (nombre= "José", servicio= "corte", dni= "3333333")]
        
        listacliente = [Cliente (nombre="Leandro", apellido="Perez", dni="40936125"), 
                    Cliente (nombre="Luciano", apellido="Mosquera ", dni="39985164"), 
                    Cliente (nombre="Mia", apellido="Garcia", dni="11111111")]    
        
        print("**************")
        print('SISTEMA DE GESTIÓN DE TURNOS')
        print("**************")
        print("--------------------------------------")
        print("MENU PRINCIPAL")
        print("--------------------------------------")

        menu = """
            [1] Registrar nuevo Cliente
            [2] Registrar nuevo Profesional
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
                #LLamada al metodo registrar_cliente de la clase Cliente para acceder a los metodos de la clase y crear objetos.
                Cliente.registrar_cliente(listacliente)

            elif opcion == "2":
                Profesionales.registrar_profesional(listaprofesionales)

            elif opcion == "3":
                Turno.solicitar_turno(gestor, listacliente, listaprofesionales)

            elif opcion == "4":
                # Envio la lista ya previamente cargada del csv.
                Turno.listar_turnos(gestor.turnos)

            elif opcion == "5":
                Turno.modificar_turno(gestor)

            elif opcion == "6":
                Turno.cancelar_turno(gestor)

            elif opcion == "7":
                #LLamada al metodo guardar_datos de la clase Gestor para acceder como una instancia a los metodos de la clase.
                gestor.guardar_datos()

            elif opcion == "8":
                gestor.guardar_datos()
                print ("Saliendo del sistema")
                break

            else: 
                print ("Opcion invalida")


mostrar_menu()