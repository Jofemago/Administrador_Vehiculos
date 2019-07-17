from modelo.BD_mantenimiento import _Mantenimiento

from negocio.tacometro import Tacometro
from negocio.vehiculo import Vehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase

import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import exists



class Mantenimiento:

    base = makeBase()

    eng = makeEngine()

    def __init__(self,id, precioMantenimiento, descripcion, fecha, idTacometro,idVehiculo):
        self.id = id
        self.precioMantenimiento = precioMantenimiento
        self.descripcion = descripcion
        self.fecha = fecha
        self.idVehiculo = idVehiculo
        self.idTacometro = idTacometro

    def eliminarByVehiculo(self, idVehiculo):
        #idVehiculo = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)
        print("ELIMINANDO mantenimientos DE VEHICULO CON ID", idVehiculo)
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        try:
            for row in ses.query(_Mantenimiento):
                if row.idVehiculo == idVehiculo:
                    ses.delete(row)
            #ses.query(_Vehiculo.nombre == name)
        except:
            print("___________NO SE PUDO ELIMINAR___________")


        ses.commit()
        ses.close()

    def getIdMax(self):

        print("obteniendo id maximo de mantenimiento para vehiculo")
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ids = [0]
        for id, in ses.query(_Mantenimiento.id).order_by(_Mantenimiento.id):
            ids.append(id)

        print("lista de ids de vehiculo:\n",ids)

        ses.close()
        return ids[-1] + 1# se retorna el primer elemento

    def makeMantenimiento(self, idVeh, descripcion, km, precioM):
        print("CREANDO MANENIMIENTO")
        print("ID DE VEHICULO", idVeh)
        fecha = datetime.date.today()
        kms = int(km)
        precio = int(precioM)
        idtacometro =Tacometro.getIdMax(Tacometro)
        newid = Mantenimiento.getIdMax(Mantenimiento)

        #Tacometro.addTacometro(Tacometro, idVeh, kms)

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        mant = _Mantenimiento(id = newid, precioMantenimiento =precio,
                                descripcion = descripcion, fecha= fecha,
                                 idTacometro =idtacometro, idVehiculo = idVeh)
        ses.add(mant)
        ses.commit()
        #res = self.makeTacometro(self, tac)
        ses.close()
