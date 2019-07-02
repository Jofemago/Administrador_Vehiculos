#from modelo.createDatabase import makeEngine, makeDatabase, makeBase
#from modelo.BD_tipoVehiculo import TipoVehiculo
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import makeEngine
from modelo.createDatabase import makeDatabase
from modelo.createDatabase import makeBase
#from modelo.BD_tipoVehiculo import makeTable as makeTableVehiculo


from modelo import BD_tipoVehiculo, BD_marcaVehiculo,BD_lineaVehiculo
from modelo import BD_combustible, BD_vehiculo, BD_tacometro
#from modelo import makeAllTables
#from modelo.BD_tipoVehiculo import _TipoVehiculo



rutaclase = "./files/clase.csv"
rutamarca = "./files/marca.csv"
rutalinea = "./files/linea.csv"

class Creator():
    base = makeBase()

    eng = makeEngine() 

    def __init__(self):
        pass

    def makeDB(self):

        makeDatabase(self.eng, self.base)

    def makeAllTables(self):

        BD_tipoVehiculo.makeTable(self.eng)
        BD_marcaVehiculo.makeTable(self.eng)
        BD_lineaVehiculo.makeTable(self.eng)
        BD_combustible.makeTable(self.eng)
        BD_vehiculo.makeTable(self.eng)
        BD_tacometro.makeTable(self.eng)

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