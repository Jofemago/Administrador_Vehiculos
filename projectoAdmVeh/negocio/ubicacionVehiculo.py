from modelo.BD_ubicacionVehiculo import _UbicacionVehiculo

from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeBase

from negocio.vehiculo import Vehiculo

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

    def eliminarByVehiculo(self, idVehiculo):
        print("ELIMINANDO TACOMETROS DE VEHICULO CON ID", idVehiculo)
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        try:
            for row in ses.query(_UbicacionVehiculo):
                if row.idvehiculo == idVehiculo:
                    ses.delete(row)
            #ses.query(_Vehiculo.nombre == name)
        except:
            print("no se pudo eliminar")


        ses.commit()
        ses.close()

    def actualizarUbicacion(self, idveh, lat, lon):
        print("actualizando la geolocalizacion")
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        for row in ses.query(_UbicacionVehiculo):
            if row.idvehiculo == idveh:
                row.latitud = lat
                row.longitud = lon
        ses.commit()
        ses.close()

    def makeUV(self, id, lat, lon):

        #lat = "4.6464"
        #lon = "-75.6117"
        print("creando la ubicacion del vehiculo_____")
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ubi = _UbicacionVehiculo(id = id, idvehiculo = id, latitud = lat, longitud = lon)
        ses.add(ubi)
        ses.commit()
        #res = self.makeVehiculo(self, veh)
        ses.close()

    def obtenerData(self):

        res = []
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        for lat, lon, id, in ses.query(_UbicacionVehiculo.latitud,_UbicacionVehiculo.longitud , _UbicacionVehiculo.idvehiculo ):
            res.append([id,lat,lon])

        ses.close()
        return res
