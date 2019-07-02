from modelo.BD_tipoVehiculo import _TipoVehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class TipoVehiculo:

    base = makeBase()

    eng = makeEngine()

    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo


    def getAllTipos(self):

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        query = None
        try:
            query = ses.query(_TipoVehiculo).all()
        except:
            print("no se puede generar la consulta")
        

        for i in query:
            print(i)

        ses.close()

        


if __name__ == "__main__":
    #tv = TipoVehiculo()
    TipoVehiculo.getAllTipos(TipoVehiculo)