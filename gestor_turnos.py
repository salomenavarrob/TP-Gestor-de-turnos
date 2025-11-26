from cliente import Cliente
from turno import Turno
import os
from db import DB 

class GestorTurnos():
    def __init__(self, archivo_csv = "turnos.csv"):
        # Inicializar el gestor de turnos con un archivo CSV para almacenar los datos.
        self.archivo_csv = archivo_csv
        # Inicializar la lista de turnos y la base de datos.
        self.turnos = []
        # Crear una instancia de la clase DB para manejar la persistencia de datos.
        self.db = DB(self.archivo_csv, Turno)
        # Cargar los turnos existentes desde el archivo CSV si existe.
        if os.path.exists (self.archivo_csv):
            self.turnos = self.db.read ()

    def modificar_turno(self, dni, nueva_fecha, nueva_hora):
        for t in self.turnos:
            if t.cliente == str(dni):
                t.fecha = nueva_fecha
                t.hora = nueva_hora
                print("Se modifica turno existente")
                return
        print("El cliente no tiene un turno registrado")

    def cancelar_turno(self, dni, fecha, hora):
        for t in self.turnos:
            if t.fecha == fecha and t.hora == hora and t.cliente == str(dni):
                self.turnos.remove(t)
                print("Se cancela turno")
                return
        print("El cliente no tiene un turno registrado")
                
    def guardar_datos(self):
        self.db.write (self.turnos)
        print("se guardan datos en archivo CSV")
    
    def registrar_turno(self, turno):
        for t in self.turnos:
            if t.fecha == turno.fecha and t.hora == turno.hora and t.profesional == turno.profesional:
                print ("Ese profesional tiene el horario ocupado")
                return 

        self.turnos.append (turno)
        print ("Turno registrado correctamente")

