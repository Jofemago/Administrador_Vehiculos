import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base



def makeEngine(name = "administradorVehiculos.db"):
    engine = create_engine('sqlite:///' + name, echo = True)
    return engine


def makeBase():
    Base = declarative_base()
    return Base

def makeDatabase(engine, base):

    #Base = declarative_base()
    base.metadata.create_all(bind =engine)


#modulos de tablas para importarlas
import BD_tipoVehiculo
import BD_marcaVehiculo
import BD_lineaVehiculo
import BD_combustible
import BD_vehiculo
import BD_tacometro

def create_all():

    eng = makeEngine()#creo el motor para poder ingresar todas las tablas


    BD_tipoVehiculo.makeTable(eng)
    BD_marcaVehiculo.makeTable(eng)
    BD_lineaVehiculo.makeTable(eng)
    BD_vehiculo.makeTable(eng)
    BD_combustible.makeTable(eng)
    BD_tacometro.makeTable(eng)


#create_all()