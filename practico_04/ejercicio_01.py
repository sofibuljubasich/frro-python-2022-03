"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3



def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Persona (IdPersona INTEGER PRIMARY KEY, Nombre VARCHAR(30), FechaNacimiento Date, DNI INT, Altura INT)''')
    
    cursor.close()
    conn.commit()
    conn.close()

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
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
