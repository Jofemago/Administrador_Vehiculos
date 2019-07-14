from modelo.BD_tacometro import _Tacometro

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import exists


class Tacometro:
    base = makeBase()

    eng = makeEngine()

    def __init__(self, id, idVehiculo, valorTacometro):

        self.id = id
        self.idVehiculo = idVehiculo
        self.valorTacometro = valorTacometro

    def eliminarByVehiculo(self, idVehiculo):
        print("ELIMINANDO TACOMETROS DE VEHICULO CON ID", idVehiculo)
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        try:
            for row in ses.query(_Tacometro):
                if row.idVehiculo == idVehiculo:
                    ses.delete(row)
            #ses.query(_Vehiculo.nombre == name)
        except:
            print("no se pudo eliminar")


        ses.commit()
        ses.close()


    def makeTacometro(self,db_tacometro):
        return Tacometro(db_tacometro.id, db_tacometro.idVehiculo,db_tacometro.valorTacometro)

    def addTacometro(self, idVehiculo, valorTacometro):

        print("AGREGANDO VALOR AL TACOMETRO________")
        newid= self.getIdMax(self,idVehiculo)
        print("nuevo id tacometro:", newid)
        tac = _Tacometro(id = newid, idVehiculo = idVehiculo, valorTacometro = valorTacometro)
        res = None
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add(tac)
        ses.commit()
        res = self.makeTacometro(self, tac)
        ses.close()

        return res

    def getIdMax(self, idvehiculo):

        print("obteniendo id maximo de tacometro para un vehiculo")
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ids = [0]
        for id, in ses.query(_Tacometro.id).order_by(_Tacometro.id):
            ids.append(id)

        print("lista de ids de vehiculo:\n",ids)

        ses.close()
        return ids[-1] + 1# se retorna el primer elemento
