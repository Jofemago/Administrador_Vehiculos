from modelo.createDatabase import makeEngine, makeDatabase, makeBase
from modelo.tipoVehiculo import TipoVehiculo,makeTableTipoVehiculo
from sqlalchemy.orm import sessionmaker


eng = makeEngine()
base = makeBase()


#makeDatabase(eng, base)
#makeTableTipoVehiculo(eng)


tipveh = TipoVehiculo(id = 1,tipo = "chevrolet")
Session = sessionmaker(bind=eng)
ses = Session() 

ses.add(tipveh)

ses.commit()