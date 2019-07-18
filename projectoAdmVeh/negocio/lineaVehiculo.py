from modelo.BD_lineaVehiculo import _LineaVehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase
from negocio.tipoVehiculo import TipoVehiculo

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



class LineaVehiculo:


    base = makeBase()

    eng = makeEngine()


    def __init__(self, id, idTipoVehiculo, idMarcaVehiculo, linea):

        self.id = id
        self.idTipoVehiculo = idTipoVehiculo
        self.idMarcaVehiculo = idMarcaVehiculo
        self.linea = linea


    def __str__(self):

        return self.linea

    def selectLinea(self, linea, listoflineas ):

        print("seleccionando linea", linea)
        for l in listoflineas:
            if l.linea == linea:
                return l

    def getAllLineas(self, marca):

        print("obtienedo linea de la marca",marca)

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        query = None
        res = []
        #query = ses.query(_MarcaVehiculo).filter(_MarcaVehiculo.idTipoVehiculo == tipo.id).all()
        try:
            query = ses.query(_LineaVehiculo).filter(_LineaVehiculo.idTipoVehiculo == marca.idTipoVehiculo, _LineaVehiculo.idMarcaVehiculo == marca.id).all()

            res = [LineaVehiculo(l.id, l.idTipoVehiculo, l.idMarcaVehiculo, l.linea) for l in query]
        except:
            print("consulta fallida")

        ses.close()

        return res