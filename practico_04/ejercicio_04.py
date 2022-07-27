"""Base de Datos SQL - Búsqueda"""
import sqlite3
import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    try:
        conn = sqlite3.connect('database.db')
        #conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Persona WHERE IdPersona = ?''',(id_persona,))
        persona = cursor.fetchone()
    except Exception as e:
        print("Error en la busqueda",e)
    finally:
        cursor.close()
        conn.close()

    if persona is None:
        return False
    else:
        return persona
    
# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    print(juan)
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
