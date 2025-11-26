from datetime import datetime

def pedir_fecha_valida(mensaje = ""):
    while True:
        fecha = input(mensaje)
        try:
            fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
            if fecha_dt.date() < datetime.now().date():
                print("No se puede usar una fecha pasada.")
                continue

            return fecha
        
        except ValueError:
            print("Formato de fecha inválido.")

def pedir_dni(mensaje = ""):
    while True:
        try:
            dni = int(input(mensaje))
            while dni < 1000000 or dni > 99999999:
                dni = int(input("Formato inválido. Ingrese entre 7 y 8 números: "))

            return dni
        
        except ValueError:
            print("Formato no válido.")

def pedir_hora_valida(mensaje = ""):
    while True:
        hora = input(mensaje)
        try:
            hora_dt = datetime.strptime(hora, "%H:%M")

            return hora

        except ValueError:
            print("Formato de hora inválido. Use HH:MM.")
