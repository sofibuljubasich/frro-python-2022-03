"""Base de Datos - Creación de Clase en ORM"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Socio(Base):
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'

    id = Column(Integer, primary_key=True)
    dni = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)

    def __init__(self, dni, nombre, apellido):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f"DNI: {self.dni}\nName: {self.nombre}\nSurname: {self.apellido}\n"


s1 = Socio(dni=11111, nombre='Jon', apellido='Snow')
s2 = Socio(dni=11321, nombre='Albus', apellido='Dumbledore')

print(s1)
print(s2)

