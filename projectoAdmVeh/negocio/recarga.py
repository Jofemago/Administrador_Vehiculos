from modelo.BD_recarga import _Recarga

from negocio.tacometro import Tacometro
from negocio.vehiculo import Vehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase

import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import exists




class Recarga:

    base = makeBase()

    eng = makeEngine()

    def __init__(id, precioCombustible,fecha, idTacometro, idVehiculo):

        self.id = id
        self.precioCombustible = precioCombustible
        self.fecha = fecha
        self.idTacometro = idTacometro
        self.idVehiculo = idVehiculo

    def eliminarByVehiculo(self, idVehiculo):
        #idVehiculo = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)
        print("ELIMINANDO recargas DE VEHICULO CON ID", idVehiculo)
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        try:
            for row in ses.query(_Recarga):
                if row.idVehiculo == idVehiculo:
                    ses.delete(row)
            #ses.query(_Vehiculo.nombre == name)
        except:
            print("___________NO SE PUDO ELIMINAR___________")


        ses.commit()
        ses.close()

    def makeRecarga(self, nombreVehiculo, precioCombustible, kilometraje):

        print("HACIENDO RECARGA DE GASOLINA, OBTENIENDO PARAMETROS NECCESARIO")
        print("VEHICULO:", nombreVehiculo)
        print("KILOMETROS", int(kilometraje))
        print("PRECIO DE LA RECARGA", precioCombustible)
        newid = self.getIdMax(self)
        preciorecarga = int(precioCombustible)
        fecha = datetime.date.today()
        #meterfechas para ahcer pruebas cuando se liste para el informe
        idtacometro =Tacometro.getIdMax(Tacometro)
        kms = int(kilometraje)

        idveh = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)
        Tacometro.addTacometro(Tacometro, idveh, kms)


        Session = sessionmaker(bind=self.eng)
        ses = Session()
        recarga = _Recarga(id = newid, precioCombustible = preciorecarga,
                            fecha = fecha, idTacometro = idtacometro,
                            idVehiculo = idveh)
        ses.add(recarga)
        ses.commit()
        #res = self.makeTacometro(self, tac)
        ses.close()

    def getIdMax(self):

        print("obteniendo id maximo de tacometro para un vehiculo")
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ids = [0]
        for id, in ses.query(_Recarga.id).order_by(_Recarga.id):
            ids.append(id)

        print("lista de ids de vehiculo:\n",ids)

        ses.close()
        return ids[-1] + 1# se retorna el primer elemento
