"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from numpy import empty
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
    

    persona = cursor.execute('''SELECT * FROM Persona WHERE IdPersona= ?''',(id_persona,)).fetchone()
    if persona is None:
        conn.commit()
        return False
    else:
        try:
            cursor.execute('''DELETE FROM Persona where IdPersona = ?''', (id_persona,))
            conn.commit()
        except sqlite3.Error as error:
            raise error

        finally:
            cursor.close()
            conn.close()
        return True
    

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
