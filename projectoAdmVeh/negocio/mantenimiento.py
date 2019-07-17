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
        #fechastr = "20/5/2018"
        #fecha = datetime.datetime.strptime(fechastr, "%d/%m/%Y").date()


        kms = int(km)
        precio = int(precioM)
        idtacometro =Tacometro.getIdMax(Tacometro)
        newid = Mantenimiento.getIdMax(Mantenimiento)

        Tacometro.addTacometro(Tacometro, idVeh, kms)

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        mant = _Mantenimiento(id = newid, precioMantenimiento =precio,
                                descripcion = descripcion, fecha= fecha,
                                 idTacometro =idtacometro, idVehiculo = idVeh)
        ses.add(mant)
        ses.commit()
        #res = self.makeTacometro(self, tac)
        ses.close()


    def getAllMtos(self,datei, datef, idv):
        print("solitando recargas para informe")
        Session = sessionmaker(bind=self.eng)
        ses = Session()

        res = []

        #DBSession.query(User).filter(User.birthday.between('1985-01-17', '1988-01-17'))
        for row in ses.query(_Mantenimiento).filter(_Mantenimiento.fecha.between(datei,datef)).filter(_Mantenimiento.idVehiculo == idv):
            #aux = [row.fecha, row.precioCombustible, ]
            res.append([row.id, row.precioMantenimiento, row.descripcion ,str(row.fecha),row.idTacometro ,row.idVehiculo])

        ses.close()
        return res
