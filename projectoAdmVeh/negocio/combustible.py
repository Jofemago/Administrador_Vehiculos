from modelo.BD_combustible import _Combustible

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class Combustible:

    base = makeBase()

    eng = makeEngine()

    def __init__(self,id, nombre, medida):

        self.id = id
        self.nombre = nombre
        self.medida = medida


    def makeC(self, db_combustible):

        return Combustible(db_combustible.id, db_combustible.nombre, db_combustible.medida)

    def __str__(self):
        return self.nombre + ":" + self.medida

    def GetCombustible(self,nameCombustible ):
        print("obteniendo combustibe of :", nameCombustible)
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        query = None
        res = None

        try:

            for row in ses.query(_Combustible).all():
                if row.nombre == nameCombustible:
                    res = row
            #query = ses.query(_Combustibles).all()
        except:
            print("no se puede generar la consulta")
        ses.close()

        return self.makeC(self,res)
