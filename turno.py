from cliente import Cliente
from registro import Registro
from datetime import datetime
from utilidad import pedir_dni, pedir_fecha_valida, pedir_hora_valida


class Turno(Registro):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return f"Cliente: {self.cliente} | Profesional: {self.profesional} | Fecha: {self.fecha} | Hora: {self.hora}"

    def listar_turnos(turnos):
        if not turnos:
            print("No hay turnos registrados.")
        else:
            for t in turnos:
                print(t)

    def solicitar_turno(gestor, lista_clientes, lista_profesionales):
        # Verificar que haya al menos un cliente y un profesional registrado.
        if not lista_clientes or not lista_profesionales:
            print("Debe haber al menos un cliente y un empleado registrado")
            return
        # Solicitar datos para el nuevo turno.
        dni = pedir_dni("Ingrese el DNI del cliente (entre 7 y 8 números): ")
        existe = any(t.dni == str(dni) for t in lista_clientes)
        if not existe:
            print(f"El cliente con DNI {dni} no esta registrado.")
            return
        
        dniProfesional = pedir_dni("Ingrese el DNI del profesional (entre 7 y 8 números): ")
        existeProfesional = any(p.dni == str(dniProfesional) for p in lista_profesionales)

        if not existeProfesional:
            print(f"El profesional con DNI {dniProfesional} no esta registrado.")
            return
        
        fecha = pedir_fecha_valida("Ingrese fecha en formato (DD/MM/YYYY): ")
        hora = pedir_hora_valida("Ingrese hora en formato (HH:MM): ")
        turno = Turno(cliente=str(dni), profesional=str(dniProfesional), fecha=fecha, hora=hora)
        gestor.registrar_turno(turno)

    def modificar_turno(gestor):
        # Solicitar DNI del cliente para modificar su turno.
        dni = pedir_dni("Ingrese el DNI del cliente (entre 7 y 8 números): ")
        # Recorrer la lista y retornar True si lo encuentra sino False.
        existe = any(t.cliente == str(dni) for t in gestor.turnos)
        
        if not existe:
            print(f"El cliente con DNI {dni} no tiene un turno registrado.")
            return
        # Solicitar nueva fecha y hora para el turno.
        nueva_fecha = pedir_fecha_valida("Ingrese nueva fecha en formato (DD/MM/YYYY): ")
        nueva_hora = pedir_hora_valida("Ingrese nueva hora en formato (HH:MM): ")
        gestor.modificar_turno(str(dni), nueva_fecha, nueva_hora)

    def cancelar_turno(gestor):
        # Solicitar DNI del cliente para cancelar su turno.
        dni = pedir_dni("Ingrese el DNI del cliente (entre 7 y 8 números): ")
        # Buscar si el cliente tiene un turno registrado.
        existe = any(t.cliente == str(dni) for t in gestor.turnos)
    
        if not existe:
            print(f"El cliente con DNI {dni} no tiene un turno registrado.")
            return
        # Solicitar fecha y hora del turno a cancelar.
        fecha = pedir_fecha_valida("Ingrese fecha del turno a cancelar en formato (DD/MM/YYYY): ")
        hora = pedir_hora_valida("Ingrese hora del turno a cancelar en formato (HH:MM): ")
        gestor.cancelar_turno(dni, fecha, hora)