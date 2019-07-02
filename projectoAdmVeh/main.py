

#Importacion de vistas
import vistas.ingresarCorreo
import vistas.administradorVentanas
import vistas.ventanaAdministradorVehiculos 
import vistas.tableroPrincipal 


#to create the database
from db.creator import Creator


from kivy.lang import Builder
from kivy.app import App


import json

pathjson = "./files/config.json"

class VistasApp(App):
	def build(self):

		#process to make the database or not, and take the mail or not
		creator = Creator()

		config = creator.makeConfigJSON()
		

		#print("La configuracion\n",config)
		if not config["init"]:
			

			#make the database
			
			creator.makeDB()
			creator.makeAllTables()
			creator.loadTipoMarcaLineaVehiculo()
			creator.loadCombustible()

			print("____________________________Creacion completa___________________________________")
			config["init"] = True
			
			creator.writeConfigJson(config)
			k=Builder.load_file("vistas.kv")


		if not config["mailvalidate"]:
			#request the mail 
			k=Builder.load_file("vistas.kv")
		else :
			k=Builder.load_file("vistas2.kv")

		return k

if __name__=="__main__":
	VistasApp().run()