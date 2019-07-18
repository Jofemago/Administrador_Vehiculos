#from modelo.createDatabase import makeEngine, makeDatabase, makeBase
#from modelo.BD_tipoVehiculo import TipoVehiculo
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeDatabase
from modelo.createDatabase import makeBase
#from modelo.BD_tipoVehiculo import makeTable as makeTableVehiculo

import requests
from modelo import BD_tipoVehiculo, BD_marcaVehiculo,BD_lineaVehiculo
from modelo import BD_combustible, BD_vehiculo, BD_tacometro, BD_ubicacionVehiculo, BD_recarga,BD_mantenimiento
#from modelo import makeAllTables
#from modelo.BD_tipoVehiculo import _TipoVehiculo
import json

#files to make the bootstraping of the
rutaclase = "./files/clase.csv"
rutamarca = "./files/marca.csv"
rutalinea = "./files/linea.csv"
pathjson = "./files/config.json"

class Creator():
    base = makeBase()

    eng = makeEngine()

    def __init__(self):
        pass

    def makeConfigJSON(self):
        config = {}
        with open(pathjson, "r") as f:
            config = json.load(f)
        f.close()
        return config

    def ConseguirPOS(self):

        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
        geo_data = geo_request.json()

        return geo_data


    def writeConfigJson(self, config):
        with open(pathjson, "w+") as filejson:
            json.dump(config , filejson , indent= 4)
        filejson.close()

    def makeDB(self):

        makeDatabase(self.eng, self.base)

    def makeAllTables(self):

        BD_tipoVehiculo.makeTable(self.eng)
        BD_marcaVehiculo.makeTable(self.eng)
        BD_lineaVehiculo.makeTable(self.eng)
        BD_combustible.makeTable(self.eng)
        BD_vehiculo.makeTable(self.eng)
        BD_tacometro.makeTable(self.eng)
        BD_ubicacionVehiculo.makeTable(self.eng)
        BD_recarga.makeTable(self.eng)
        BD_mantenimiento.makeTable(self.eng)

    def loadTipoMarcaLineaVehiculo(self):
        self.loadTipo()
        self.loadMarca()
        self.loadLinea()


    def loadLinea(self):

        lineas = []
        with open(rutalinea) as ins:
            for line in ins:
                lineas.append(line.replace('\n',""))
        lineas = lineas[1:]

        for i in range(len(lineas)):
            lineas[i] = lineas[i].split(",")[1:]

        elementstoUpload = [BD_lineaVehiculo._LineaVehiculo(id = l[0], idTipoVehiculo = l[1] , idMarcaVehiculo = l[2] , linea = l[3]) for l in lineas]
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add_all(elementstoUpload)
        ses.commit()
        ses.close()

    def addVehiculesPrueba(self):

        prueba1 = BD_vehiculo._Vehiculo(id = 2, nombre = "veh1", idLineaVehiculo = 1, idCombustible = 1)
        prueba2 = BD_vehiculo._Vehiculo(id = 1, nombre = "veh2", idLineaVehiculo = 1, idCombustible = 1)
        prueba3 = BD_vehiculo._Vehiculo(id = 3, nombre = "veh3", idLineaVehiculo = 1, idCombustible = 1)

        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add_all([prueba1, prueba2, prueba3])
        ses.commit()
        ses.close()

    def loadCombustible(self):
        l = [[1,"Gasolina", "galones"],[2, "Diesel", "Galones"],[3, "Gas", "m3"], [4, "ACPM", "galones"]]
        elementstoUpload = [BD_combustible._Combustible(id = c[0], nombre = c[1], medida = c[2]) for c in l]
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add_all(elementstoUpload)
        ses.commit()
        ses.close()


    def loadMarca(self):

        marcas = []
        with open(rutamarca) as ins:
            for line in ins:
                marcas.append(line.replace('\n',""))
        marcas = marcas[1:]

        for i in range(len(marcas)):
            marcas[i] = marcas[i].split(",")[1:]

        elementstoUpload = [BD_marcaVehiculo._MarcaVehiculo(id = m[0], idTipoVehiculo = m[1], marca = m[2]) for m in marcas]
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add_all(elementstoUpload)
        ses.commit()
        ses.close()



    def loadTipo(self):
        clases = []
        with open(rutaclase) as ins:
            for line in ins:
                clases.append(line.replace('\n', ""))
        clases = clases[1:]

        for i in range(len(clases)):
            clases[i] = clases[i].split(",")[1:]
        #print(clases)
        elementstoUpload = [BD_tipoVehiculo._TipoVehiculo(id = c[0],tipo = c[1]) for c in clases]
        Session = sessionmaker(bind=self.eng)
        ses = Session()
        ses.add_all(elementstoUpload)
        ses.commit()
        ses.close()



#c = Creator()
#c.makeAllTables()

#tipveh = _TipoVehiculo(id = 2,tipo = "chevrolet")


"""

try:
    Session = sessionmaker(bind=eng)
    ses = Session()


    ses.add(tipveh)

    ses.commit()
except Exception:
    print(Exception)


"""
