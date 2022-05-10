"""Propiedades"""


class Auto:
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    def __init__(self, marca, precio=0):
        self.__marca = marca
        self.__precio = precio

    def __str__(self):
        marca = self.__marca.title()
        first_letter = marca.capitalize()
        return f"Marca: {first_letter[0:1]}\nPrecio: {self.precio}"

    def _get_marca(self):
        return self.__marca

    def _get_precio(self):
        return round(self.__precio, 2)
    
    def _set_precio(self, value):
        self.__precio = value
    
    marca = property(
        fget=_get_marca,
    )

    precio = property(
        fget=_get_precio,
        fset=_set_precio,
    )
# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)
print(auto)
assert auto.marca == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.marca = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    """Re-Escribir utilizando DataClasses"""

    marca: str
    precio: float

    def get_marca(self):
        return self.marca

    @property
    def get_precio(self):
        return round(self.precio, 2)

    @property
    def set_precio(self, value):
        self.precio = value


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)
print(auto)
assert auto.marca == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN'''
