#from modelo.createDatabase import makeEngine, makeDatabase, makeBase
#from modelo.BD_tipoVehiculo import TipoVehiculo
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import makeEngine
#from modelo.makeAllTables import create_all

"""
import BD_tipoVehiculo
import BD_marcaVehiculo
import BD_lineaVehiculo
import BD_combustible
import BD_vehiculo
import BD_tacometro



create_all()
"""

eng = makeEngine()
"""
base = makeBase()


#makeDatabase(eng, base)
#makeTableTipoVehiculo(eng)


tipveh = TipoVehiculo(id = 1,tipo = "chevrolet")
Session = sessionmaker(bind=eng)
ses = Session()

ses.add(tipveh)

ses.commit()
"""
