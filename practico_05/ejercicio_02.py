from setuptools import find_namespace_packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio
from sqlalchemy.ext.declarative import declarative_base

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base = declarative_base(engine)
        Base.metadata.create_all(engine, tables=Socio.__tablename__)

        db_session = sessionmaker(bind = engine)
        self.session = db_session()

            

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        #first()--> Returns None or the row
        try:
            socio = self.session.query(Socio).filter(Socio.id_socio == id_socio).first()
        except Exception as e:
            print("Error: ",e)
        finally:
            self.session.close()
        return socio

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        try:
            socio = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        except Exception as e:
            print("Error: ",e)
        finally:
            self.session.close()
    
        return socio
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        try:
            socios = self.session.query(Socio).all()
        except Exception as e:
            print("Error: ",e)
        finally:
            self.session.close()
        return socios

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        try:
            self.session.query(Socio).all().delete()
            self.session.commit()
            rta = True
        except:
            rta = False
        finally:
            self.session.close()
        return rta



    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        try:

            self.session.add(socio)
            self.session.commit()
        except Exception as e:
            print("Error en el alta: ",e)
        finally:
            self.session.close()

        return socio
    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        try:
            self.session.query(Socio).filter(Socio.id_socio == id_socio).delete()
            rta = True
        except:
            self.session.rollback()
            rta = False
        finally:
           
            self.session.commit()
            self.session.close()
        return rta

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        try:
            self.session.query(Socio).filter(Socio.id_socio == socio.id_socio).update({'dni': socio.dni,'nombre':socio.nombre,'apellido':socio.apellido})
            self.session.commit()
        except:
            self.session.rollback()
        finally:
            self.session.close()

        return socio
        
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        rows = self.session.query(Socio).count()
        return rows





# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN