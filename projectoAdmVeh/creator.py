#from modelo.createDatabase import makeEngine, makeDatabase, makeBase
#from modelo.BD_tipoVehiculo import TipoVehiculo
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeDatabase
from modelo.createDatabase import makeBase
#from modelo.BD_tipoVehiculo import makeTable as makeTableVehiculo


from modelo import BD_tipoVehiculo, BD_marcaVehiculo,BD_lineaVehiculo
from modelo import BD_combustible, BD_vehiculo, BD_tacometro
#from modelo import makeAllTables
#from modelo.BD_tipoVehiculo import _TipoVehiculo


class Creator():
    base = makeBase()

    eng = makeEngine() 

    def __init__(self):
        pass

    def makeDB(self):

        makeDatabase(self.eng, self.base)

    def makeAllTables(self):

        BD_tipoVehiculo.makeTable(self.eng)
        BD_marcaVehiculo.makeTable(self.eng)
        BD_lineaVehiculo.makeTable(self.eng)
        BD_combustible.makeTable(self.eng)
        BD_vehiculo.makeTable(self.eng)
        BD_tacometro.makeTable(self.eng)


#c = Creator()
#c.makeAllTables()

#tipveh = _TipoVehiculo(id = 2,tipo = "chevrolet")


"""

try:
    Session = sessionmaker(bind=eng)
    ses = Session()


    ses.add(tipveh)

    ses.commit()
except Exception:
    print(Exception)


"""