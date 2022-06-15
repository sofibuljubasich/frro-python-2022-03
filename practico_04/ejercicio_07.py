"""Base de Datos SQL - Uso de múltiples tablas"""
import datetime
import sqlite3
from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    persona = buscar_persona(id_persona)

    if persona is not False:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT MAX(fecha) FROM PersonaPeso WHERE idPersona = ? GROUP BY idPersona''', (id_persona,))
        last_date = cursor.fetchone()
        if fecha > last_date:
            cursor.execute('''INSERT INTO PersonaPes(id_persona,fecha, peso) VALUES(?,?,?)''', (id_persona, fecha, peso))
            cursor.close()
            conn.commit()
            conn.close()
            return id_persona
        else:
            conn.close()
            return False
    else:
        return False


       


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    #print(agregar_peso(id_juan, datetime.datetime.date().today(), 100))
    #print(id_juan)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
