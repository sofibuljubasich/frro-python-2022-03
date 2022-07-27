"""Variables y Métodos de Clase"""


class Articulo:

    idIncrement = 1
    
    """Clase con "nombre" como variable de instancia y un id incremental
    generado automáticamente.

    Restricciones:
        - Utilizar sólamente el constructor (__init__) y un método de
          clase (@classmethod) con una variable de clase
    """

    def __init__(self, nombre='unknown'):
        self.nombre = nombre
        self.id = Articulo.idIncrement
        Articulo.idIncrement += 1
        

    @classmethod
    def last_id(cls):
        
        return cls.idIncrement-1
        


# NO MODIFICAR - INICIO
art1 = Articulo("manzana")
art2 = Articulo("pera")
art3 = Articulo()
art3.nombre = "tv"

assert art1.nombre == "manzana"
assert art2.nombre == "pera"
assert art3.nombre == "tv"

assert art1.id == 1
assert art2.id == 2
assert art3.id == 3
assert Articulo.last_id() == 3
# NO MODIFICAR - FIN
