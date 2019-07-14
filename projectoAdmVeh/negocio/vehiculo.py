from modelo.BD_vehiculo import _Vehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import exists


class Vehiculo:

    base = makeBase()

    eng = makeEngine()

    def __init__(self, id, nombre, idLineaVehiculo, idCombustible):

        self.id = id
        self.nombre = nombre
        self.idLineaVehiculo = idLineaVehiculo
        self.idCombustible = idCombustible


    def makeVehiculo(self, db_vehiculo):

        return Vehiculo(db_vehiculo.id , db_vehiculo.nombre, db_vehiculo.idLineaVehiculo, db_vehiculo.idCombustible)


    def existeVehiculo(self, vehiculo):

        print("verificando existencia de:", vehiculo)
        Session = sessionmaker(bind=self.eng)
        ses = Session()

        #make validation
        for nombre, in ses.query(_Vehiculo.nombre):
            if nombre == vehiculo:
                ses.close()
                return True
        #print("sale del ciclo______________")
        ses.close()
        return False


    def getIdMax(self):

        print("obteniendo id maximo de vehiculo")
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ids = [0]
        for id, in ses.query(_Vehiculo.id).order_by(_Vehiculo.id):
            ids.append(id)

        print("lista de ids de vehiculo:\n",ids)

        ses.close()
        return ids[-1] + 1# se retorna el primer elemento

    def getIdvehiculo(self, name):

        print("obteniendo id del vehiculo:", name)
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        res = None
        for id, nombre, in ses.query(_Vehiculo.id, _Vehiculo.nombre):
            if nombre == name:
                res = id
                break


        ses.close()
        print("id del vehiculo" ,name, "es:", res)
        return res

    def addVehiculo(self, nombre, idLineaVehiculo, idCombustible):

        print("Añadiendo vehiculo___________:")
        newid = self.getIdMax(self)
        print("NEW ID-------,", newid)

        veh = _Vehiculo(id = newid, nombre = nombre, idLineaVehiculo = idLineaVehiculo, idCombustible = idCombustible)
        res = None
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add(veh)
        ses.commit()
        res = self.makeVehiculo(self, veh)
        ses.close()

        return res

    def listarNameVehiculos(self):

        print("Obteniendo la totalidad de los equipos")
        res = []
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        for id, nombre, idLineaVehiculo, idCombustible, in ses.query(_Vehiculo.id, _Vehiculo.nombre, _Vehiculo.idLineaVehiculo, _Vehiculo.idCombustible):
            res.append(Vehiculo(id, nombre, idLineaVehiculo, idCombustible))

        ses.close()
        return res


    def deleteVehiculo(self, name):

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        try:
            for row in ses.query(_Vehiculo):
                if row.nombre == name:
                    ses.delete(row)
            #ses.query(_Vehiculo.nombre == name)
        except:
            print("no se pudo eliminar")


        ses.commit()
        ses.close()





#stmt = exists().where(Address.user_id==User.id)
