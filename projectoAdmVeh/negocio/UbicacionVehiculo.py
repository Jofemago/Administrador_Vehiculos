from modelo.BD_ubicacionVehiculo import _UbicacionVehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import exists


class UbicacionVehiculo:

    base = makeBase()

    eng = makeEngine()

    def __init__(self, id, idvehiculo, latitud, longitud):
        self.id = id
        self.idvehiculo = idvehiculo
        self.latitud = latitud
        self.longitud = longitud
