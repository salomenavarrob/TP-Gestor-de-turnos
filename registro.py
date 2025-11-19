class Registro(object):
    """Clase base que representa un registro genérico de la base de datos"""
    def __init__(self, **kwargs):
        # **kwargs nos permite recibir cualquier cantidad de argumentos con nombre
        # Los asignamos como atributos del objeto
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)
    
    def __str__(self):
        """Representación en string del objeto"""
        atributos = []
        for clave, valor in self.__dict__.items():
            atributos.append(f"{clave}: {valor}")
        clase = self.__class__.__name__  # Obtiene el nombre de la clase actual
        return f"{clase}({', '.join(atributos)})"

