from registro import Registro 
from transforma import Transforma 
from cliente import Cliente

class DB(object):
    def __init__(self, filename, tipo_registro=None):
        self.filename = filename
        self.tipo_registro = tipo_registro or Registro
    
    def read(self):
        db = []
        file = open(self.filename, "rt")
        line = file.readline() # Leo encabezado

        if line == "":
            return db
        keys = line.split(",") 
        tran = Transforma(keys, self.tipo_registro)
        line = file.readline() # Leo la primera linea
        while line != "":
            values = line.split(",")
            # Ahora creamos objetos del tipo especificado
            obj = tran.toObject(values)
            if obj:  # Solo agregamos si el objeto se creó correctamente
                db.append(obj)
            line = file.readline()
        file.close()
        return db

    def write(self, registros):
        if not registros:
            return
        
        with open (self.filename, "wt") as file:
            #escribir encabezado
            keys = list (registros [0].__dict__.keys())
            file.write (",".join (keys) + "\n" )
            #escribir registros
            for r in registros:
                values = [str (getattr (r, k)) for k in keys] 
                file.write (",".join (values) + "\n" )

    @classmethod
    def crear_db_clientes(cls, filename):
        """Método de clase para crear una DB específica para clientes"""
        return cls(filename, Cliente)

