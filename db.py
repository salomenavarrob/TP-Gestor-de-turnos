from registro import Registro 
from transforma import Transforma 
from cliente import Cliente

class DB(object):
    def __init__(self, filename, tipo_registro=None):
        self.filename = filename
        self.tipo_registro = tipo_registro or Registro
        
    # csv crea dic tran obj
    def read(self):
        db = []
        # Abrir el archivo en modo lectura de texto.
        file = open(self.filename, "rt")
        # Leer la primera línea (encabezado).
        line = file.readline() 
        # Si el archivo está vacío, retornar una lista vacía.
        if line == "":
            return db
        # Procesar el encabezado para obtener las claves de los atributos.
        keys = line.split(",") 
        tran = Transforma(keys, self.tipo_registro)
        # Leer las líneas restantes y crear objetos.
        line = file.readline()
        # Bucle hasta el final del archivo.
        while line != "":
            values = line.split(",")
            # Ahora creamos objetos del tipo especificado
            obj = tran.toObject(values)
            # Solo agregar si el objeto se creó correctamente
            if obj:  
                db.append(obj)
            # Leer la siguiente línea.
            line = file.readline()
        file.close()
        return db

#objeto tran dic crea csv
    def write(self, registros):
        # Si la lista de registros está vacía, no hacer nada.
        if not registros:
            return
        # Abrir el archivo en modo escritura de texto.
        with open (self.filename, "wt") as file:
            # Escribir encabezado.
            keys = list (registros [0].__dict__.keys())
            file.write (",".join (keys) + "\n" )
            # Escribir registros.
            for r in registros:
                values = [str (getattr (r, k)) for k in keys] 
                file.write (",".join (values) + "\n" )
