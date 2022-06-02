"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

conn = sqlite3.connect('practica4.db')

cursor = conn.cursor()

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conn.execute('''CREATE TABLE Persona (IdPersona int PRIMARY KEY, Nombre Char(30), FechaNacimiento text, DNI int, Altura int)''')
    conn.commit()
    conn.close()

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn.execute('''DROP TABLE Persona''')
    conn.commit()
    conn.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
