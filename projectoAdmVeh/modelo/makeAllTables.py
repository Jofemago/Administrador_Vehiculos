import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base






#modulos de tablas para importarlas
#from createDatabase import makeEngine
#from createDatabase import makeDatabase
from BD_tipoVehiculo import _TipoVehiculo
from BD_tipoVehiculo import makeTable as maketipov
#import BD_marcaVehiculo
#import BD_lineaVehiculo
#import BD_combustible
#import BD_vehiculo
#import BD_tacometro

class create_all():
    def __init__(self, eng):
        #eng = makeEngine()#creo el motor para poder ingresar todas las tablas
        maketipov(eng)
        #BD_tipoVehiculo.makeTable(eng)
        #BD_marcaVehiculo.makeTable(eng)
        #BD_lineaVehiculo.makeTable(eng)
        #BD_vehiculo.makeTable(eng)
        #BD_combustible.makeTable(eng)
        #BD_tacometro.makeTable(eng)


#create_all()