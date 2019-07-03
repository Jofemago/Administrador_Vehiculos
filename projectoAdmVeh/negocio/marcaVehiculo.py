from modelo.BD_marcaVehiculo import _MarcaVehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase
from negocio.tipoVehiculo import TipoVehiculo

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



class MarcaVehiculo:

    base = makeBase()

    eng = makeEngine()


    def __init__(self, id, idTipoVehiculo, marca):

        self.id = id
        self.idTipoVehiculo = idTipoVehiculo
        self.marca = marca


    def __str__(self):

        return self.marca

    def getAllMarcas(self, tipo):
        
        print("obtienedo marca del tipo",tipo)

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        query = None
        res = []
        #query = ses.query(_MarcaVehiculo).filter(_MarcaVehiculo.idTipoVehiculo == tipo.id).all()
        try:
            query = ses.query(_MarcaVehiculo).filter(_MarcaVehiculo.idTipoVehiculo == tipo.id).all()

            res = [MarcaVehiculo(m.id, m.idTipoVehiculo, m.marca) for m in query]
        except:
            print("consulta fallida")

        ses.close()

        return res


    def selectMarca(self, marca, listofmarcas):
        print("seleccionano marca:", marca)
        for m in listofmarcas:
            if m.marca == marca:
                return m

