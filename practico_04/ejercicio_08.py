"""Base de datos SQL - Listar"""

import datetime
import sqlite3

from numpy import empty
from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_07 import agregar_peso
from ejercicio_04 import buscar_persona


def listar_pesos(id_persona):
    """Implementar la funcion listar_pesos, que devuelva el historial de pesos 
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
     mplementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente 
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """
    persona = buscar_persona(id_persona)
    if persona is not False:
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            pesos = cursor.execute('''SELECT Fecha,Peso FROM PersonaPeso WHERE idPersona = ?''', (id_persona,)).fetchall()

        except Exception as e:
            print("Error al buscar registros", e)
        finally:
            cursor.close()
            conn.close()
    else:
        return False
    if pesos is not empty:
        return pesos
    else:
        return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    print(pesos_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
