from registro import Registro 

class Transforma(object):
    def __init__(self, atributos, tipo_registro=None):
        self.keys = atributos
        self.tipo_registro = tipo_registro or Registro  # Por defecto usa Registro genérico

    def toDict(self, values):
        if len(values) != len(self.keys):
            return None
        d = {}
        i = 0
        while i < len(values):
            d[self.keys[i]] = values[i]
            i = i + 1
        return d
    
    def toObject(self, values):
        """Convierte una lista de valores en un objeto del tipo especificado"""
        if len(values) != len(self.keys):
            return None
        
        # Creamos un diccionario para usar como **kwargs
        datos = {}
        i = 0
        while i < len(values):
            # Limpiamos los valores (quitamos saltos de línea)
            valor_limpio = values[i].strip()
            datos[self.keys[i].strip()] = valor_limpio
            i = i + 1
        
        # Creamos el objeto del tipo especificado usando **kwargs
        obj = self.tipo_registro(**datos)
        
        return obj