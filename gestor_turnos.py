from cliente import Cliente
from turno import Turno
import os
from db import DB 

class GestorTurnos():
    def __init__(self, archivo_csv = "turnos.csv"):
        self.archivo_csv = archivo_csv
        self.turnos = []  # lista de objetos Turno
        self.db = DB (self.archivo_csv)
        if os.path.exists (self.archivo_csv):
            self.turnos = self.db.read ()

    def listar_turnos(self):
        if not self.turnos:
            print("No hay turnos registrados.")
        else:
            for t in self.turnos:
                print(t)


# Métodos del gestor 

    def registrar_turno(self, turno):
        for t in self.turnos:
            if t.fecha == turno.fecha and t.hora == turno.hora:
                print ("Ese horario ya está ocupado")
                return 

        self.turnos.append (turno)
        print ("Turno registrado correctamente")

    def modificar_turno(self, dni, nueva_fecha, nueva_hora):
        for t in self.turnos:
            if t.cliente == dni:
                t.fecha = nueva_fecha
                t.hora = nueva_hora
                print ("Se modifica turno existente")
                return
            else:
                print ("El cliente no tiene un turno registrado")

    def cancelar_turno(self, dni, fecha, hora):
        for t in self.turnos:
            if t.fecha == fecha and t.hora == hora and t.cliente == dni:
                self.turnos.remove (t)
                print("Se cancela turno")
            else:
                print ("El cliente no tiene un turno registrado")
                
    def guardar_datos(self):
        self.db.write (self.turnos)
        print("se guardan datos en archivo CSV")
    


