from kivy.lang import Builder
from kivy.uix.screenmanager import Screen 
from kivy.clock import Clock
from  kivy.uix.relativelayout import RelativeLayout
from kivy.garden.mapview import MapView, MapSource, MapMarker, MapMarkerPopup
from kivy.uix.bubble import Bubble
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random
import requests

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

root = Builder.load_string("""
#:import MapSource kivy.garden.mapview.MapSource

<Toolbar@BoxLayout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'

    canvas:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<ShadedLabel@Label>:
    size: self.texture_size
    canvas.before:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<VentanaGPS>:
	name: "gps"
	BoxLayout:
		BoxLayout:
			RelativeLayout:

			    MapView:
			        id: mapview
			        lat: 4.5330700
			        lon: -75.7043800
			        zoom: slider.value
			        #size_hint: .5, .5
			        #pos_hint: {"x": .25, "y": .25}

			        #on_map_relocated: mapview2.sync_to(self)
			        #on_map_relocated: mapview3.sync_to(self)


			    Toolbar:
			        top: root.top
			        Button:
			            text: "Actualizar Vehiculos"
			            on_release: root.actualizarMarcadores()
			        Button:
			            text: "Restaurantes"
			            on_release: root.eliminarMarcadores()
			        Button:
			            text: "Parqueaderos"
			            on_release: root.eliminarMarcadores()

			    Toolbar:
			        Label:
			            text: "Longitude: {}".format(mapview.lon)
			        Label:
			            text: "Latitude: {}".format(mapview.lat)
				    Button:
				    	text: "Regresar"
				    	on_release: 
				    		root.manager.current= "segunda"
				    		root.manager.transition.direction = "right"

		BoxLayout:
			size_hint_x: 0.07
		    Slider:
		        id: slider
		        min: 1
		        max: 20
		        step: 1
		        value: 10
		        orientation: 'vertical'

    """)

class VentanaGPS(Screen):
	listaMarker=[] 
	def __init__(self, **kwargs):
		super(VentanaGPS, self).__init__(**kwargs)
		Clock.schedule_once(lambda dt:self.actualizarMarcadores())

	def actualizarMarcadores(self): #Muestro los marcadores con las ubicaciones actualizadas en el mapa
		ip_request = requests.get('https://get.geojs.io/v1/ip.json')
		my_ip = ip_request.json()['ip'] #con mi ip obtengo mi geolocalizacion
		geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
		geo_data = geo_request.json()

		self.ids.mapview.center_on(float(geo_data['latitude']), float(geo_data['longitude'])) #mapa centrado en ubicacion actual

		mapmarkerpopup=MapMarkerPopup(lat= float(geo_data['latitude']),lon= float(geo_data['longitude']), popup_size= (120,70))
		bubble=Bubble()
		label= Label(text= "[b]Ubicaion actual![/b]", markup= True, halign= "center")
		bubble.add_widget(label)
		mapmarkerpopup.add_widget(bubble) #creo un marcador con etique para saber la ubicacion actual, es de color rojo
		

		if len(self.listaMarker)>0:
		    for marker in range(len(self.listaMarker)):
		        self.ids.mapview.remove_widget(self.listaMarker[marker])
		    self.listaMarker=[] #La reseteo para poder meter los mapMarker de los vehiculos actualizados.

		#Se hace la consulta a la BD para obtener las lat y lon de los vehiculos-----------------------BD
		self.listaMarker.append(mapmarkerpopup)
		for l in range(10):
			mapmarkerpopup=MapMarkerPopup(lat=random.randint(1, 5), lon=-75.7043800+l/2, color=(0,1,1,1), popup_size= (120,70))
			bubble=Bubble()
			label= Label(text= "[b]Ubicaion actual![/b]", markup= True, halign= "center")
			bubble.add_widget(label)
			mapmarkerpopup.add_widget(bubble)
			self.listaMarker.append(mapmarkerpopup)
		for i in range(10):
		    self.ids.mapview.add_widget(self.listaMarker[i])

	def eliminarMarcadores(self): #al presionar restaurantes o parqueaderos, borro los marcadores del mapa
		for marker in range(len(self.listaMarker)):
			self.ids.mapview.remove_widget(self.listaMarker[marker])
		self.listaMarker=[]
