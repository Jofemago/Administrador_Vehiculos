from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder
import requests

#import from another views
from vistas.anadirVehiculo import AgregarVehiculo

#importando desde el packete db
from db.creator import Creator

#import desde negocio
from negocio.tipoVehiculo import TipoVehiculo
from negocio.vehiculo import Vehiculo
from negocio.tacometro import Tacometro

"""
Los botones de vehiculo, Ubicacion y Eliminar los implemento como clases aparte, esto con el objeto de poder obtener la instancia de cada
btn al presionar uno, ya que desde el kv solo es mandar como parametro a la funcion (self) si el btn es presionado, hay otras formas,
pero no quiero, con esto puedo obtener el id correspondiente al vehiculo.
"""
#l=[]

k=Builder.load_string("""
<SecondWindow>:
    name: "segunda"
    BoxLayout:
        id:box
        orientation:"vertical"
        BoxLayout:
            size_hint_y:0.3
            orientation:"vertical"
            Label:
                text: "Administrador de vehiculos"
            BoxLayout:
                Label:
                    text: "Veiculo"
                Label:
                    text: "Ubicacion"
                Label:
                    text: "Eliminar"
        ScrollView:
            id: scroll
            GridLayout:
                id: contenedorFilas
                cols: 1
                size_hint_y: None #Si esto no se pone, el scroll no aparece.
                row_default_height: root.height*0.1
                height: self.minimum_height
        BoxLayout:
            size_hint_y:0.25
            spacing: 50
            padding: 20,30,50,10 #Margenes: izquierda, arriba, derecha, abajo
            Button:
                text: "Agregar Vehiculo"
                on_release:
                	root.oprimidoBtnAgregarVehiculo()
            Button:
                text: "GPS"
                on_release:

                    root.manager.current = "gps"

<BotonVehiculo>:
    on_press: root.changeWindows(app)
<BotonUbicacion>:
    on_press: root.ubicacionVehiculo()
<BotonEliminar>:
    on_press: root.eliminarVehiculo()
""")
class BotonVehiculo(Button):
    def changeWindows(self,app):
        c = Creator()
        json = c.makeConfigJSON()
        print("PASO DE VENTANA_____VEHICULO:",self.parent.children[2].text)
        json["nameVehicule"] = self.parent.children[2].text
        c.writeConfigJson(json)
        app.root.current="tableroPrincipal"
        print(app.root.screens[1].name)
        for i in app.root.screens:
            if i.name == "tableroPrincipal":
                i.confCorreo()
        #app.root.screens[1].confCorreo()

class BotonUbicacion(Button):
    def ubicacionVehiculo(self):

        #integracion base de datos
        nombre = self.parent.children[2].text
        print ("ubicar vehiculo", nombre)#bd
        print("id vehiculo: ", Vehiculo.getIdvehiculo(Vehiculo, nombre))

        """
        #lo que hizo pareja
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
        geo_data = geo_request.json()

        #Agregar ubicacion DB
        print(self.parent.children[2].text) #Para obtener el nombre del vehiculo.
        print(geo_data['latitude'], geo_data['longitude'])
        """
        self.popup = Popup(title="ESTADO",content=Label(text="Ubicacion guardada correctamente"),size_hint=(0.7, 0.2))
        self.popup.open()


class BotonEliminar(Button):

    def eliminarVehiculo(self):
        nombre = self.parent.children[2].text
        idvehiculo = Vehiculo.getIdvehiculo(Vehiculo,nombre)
        print("VEHICULO ID, eliminando.................:", nombre , idvehiculo )
        Vehiculo.deleteVehiculo(Vehiculo,nombre)
        Tacometro.eliminarByVehiculo(Tacometro, idvehiculo)
        #aqui eliminar las recargas, los mantenimientos, las ubicacionnes, tacometros que tengan el id del vehiculo
        self.parent.parent.remove_widget(self.parent)

class SecondWindow(Screen):
	#l=[]
	def __init__(self, **kwargs):
		super(SecondWindow, self).__init__(**kwargs)
		Clock.schedule_once(lambda dt:self.scrollVehiculos())
		self.vehiculosinapp = []
        #lista de todos los vehiculos



	def oprimidoBtnAgregarVehiculo(self):
		self.content = AgregarVehiculo() #Este texto que paso lo captura el stringProperty
		self.content.bind(on_guardar=self._on_guardar) #segun mi analisis, es para dar el mando de on_answer a _on_answer
		self.popup = Popup(title="Agregue el vehiculo que desee",
							content=self.content,
							size_hint=(0.9, 0.9))
		self.popup.open()

	def _on_guardar(self, instance):
		#print("instance:", instance)
		resultadoVentanaAgregarVehiculo=self.content.on_guardar() #La pos 0 me determina si los datos de agregarVeh son correctos o no.
		if resultadoVentanaAgregarVehiculo[0]: #pos que contiene True o False
			self.vehiculosinapp.append(resultadoVentanaAgregarVehiculo[2])
			box=BoxLayout(orientation="horizontal")
			box.add_widget(BotonVehiculo(text=resultadoVentanaAgregarVehiculo[1])) #pos que tiene nombre del vehiculo.
			box.add_widget(BotonUbicacion(text="ubicacion")) #Los ids son iguales y corresponden al nombre del vehiculo
			box.add_widget(BotonEliminar(text="Eliminar"))
			self.ids.contenedorFilas.add_widget(box)
			self.popup.dismiss()
		else:
			pass

	def scrollVehiculos(self):
		# CONSULTA BASE DE DATOS PARA LISTAR TODOS LOS VEHICULOS
		for e in Vehiculo.listarNameVehiculos(Vehiculo):
			self.vehiculosinapp.append(e)
		#self.vehiculosinapp.append()
		for i in range(len(self.vehiculosinapp)):
			#print(self.vehiculosinapp)
			#self.l.append(BoxLayout(orientation="horizontal"))
			#self.ids.contenedorFilas.add_widget(self.l[-1]) #al gridlayout le agrego lo boxlayout necesarios, en cada boxlayout puedo posicionar
															 #mis tres botones.
			self.ids.contenedorFilas.add_widget(BoxLayout(orientation="horizontal"))
		for i, n in enumerate(self.ids.contenedorFilas.children):
			n.add_widget(BotonVehiculo(text=(self.vehiculosinapp[i].nombre)))
			n.add_widget(BotonUbicacion(text="ubicacion")) #Los ids son iguales y corresponden al nombre del vehiculo
			n.add_widget(BotonEliminar(text="Eliminar"))


			#l.append(n)
		#l.append(self.ids.contenedorFilas)
		#print(l) #No entiendo porque se imprimen dos listas

	"""
	#Esta funcion la dejo por si algo, no funciono para eliminar los botones, pero fue un intento que depronto me sirva en el futuro.
	def eliminarVehiculo(self, idBoton): #esto es para eliminar los botones asociados a un boxL pero sale raro, creo que es porque meto los
										 #boxLayout a una lista, o porque el parametr idBoton me lo pasan desde otra clase.
		#print(idBoton)
		#self.l[int(idBoton)].clear_widgets()
		#self.ids.contenedorFilas.remove_widget(self.l[int(idBoton)])
		#self.l.pop(int(idBoton))
	"""
