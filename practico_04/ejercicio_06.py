"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    try:
        
        conn = sqlite3.connect('database.db')

        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS PersonaPeso
        (idPersona,Fecha Date,Peso Int, FOREIGN KEY(idPersona) REFERENCES Persona(IdPersona))''')
        conn.commit()
    except Exception as e:
        print("Error al crear tabla",e)
    finally:
        cursor.close()
        conn.close()
        

def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    try:
        conn = sqlite3.connect('database.db')

        cursor = conn.cursor()
        conn.execute('''DROP TABLE PersonaPeso''')
        conn.commit()
    except Exception as e:
        print("Error al borrar tabla",e)
    finally:
        cursor.close()
        conn.close()
    


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
