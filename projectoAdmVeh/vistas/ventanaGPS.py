from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from  kivy.uix.relativelayout import RelativeLayout
from kivy.garden.mapview import MapView, MapSource, MapMarker, MapMarkerPopup
from kivy.uix.bubble import Bubble
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random
import requests #para solicitar mi ubicacion
#from pandas.io.json import json_normalize #para obtener organizadamente lugares cercanos a mi ubicacion

#librerias de Felipe
from db.creator import Creator
from negocio.ubicacionVehiculo import UbicacionVehiculo
from negocio.vehiculo import Vehiculo

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
			        zoom: 8
			        #size_hint: .5, .5
			        #pos_hint: {"x": .25, "y": .25}

			        #on_map_relocated: mapview2.sync_to(self)
			        #on_map_relocated: mapview3.sync_to(self)


			    Toolbar:
			        top: root.top
			        Button:
			            text: "Actualizar Vehiculos"
			            on_release: root.visualizarVehiculos()
			        Button:
			            text: "Lugares cercanos"
			            on_release: root.lugaresParaUbicacionActual()

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

    """)

class VentanaGPS(Screen):
    listaMarker=[] #Me permite quitar solo los marcadores de los vehiculos que estan en el mapa, aca se referencian.
    longitudActual=0.0
    latitudActual=0.0
    def __init__(self, **kwargs):
    	super(VentanaGPS, self).__init__(**kwargs)
    	Clock.schedule_once(lambda dt:self.visualizarVehiculos())

    def visualizarVehiculos(self): #Muestro los marcadores con las ubicaciones actualizadas en el mapa
    	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    	my_ip = ip_request.json()['ip'] #con mi ip obtengo mi geolocalizacion
    	geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    	geo_data = geo_request.json()

    	self.longitudActual=float(geo_data['longitude'])
    	self.latitudActual=float(geo_data['latitude'])

    	self.ids.mapview.center_on(self.latitudActual, self.longitudActual) #mapa centrado en ubicacion actual
    	self.ids.mapview.zoom=5
    	"""
    	mapmarkerpopupUbicacionActual=MapMarkerPopup(lat= self.latitudActual,lon= self.longitudActual, popup_size= (120,70))
    	bubbleUbicacionActual=Bubble()
    	labelUbicacionActual= Label(text= "[b]Ubicaion actual![/b]", markup= True, halign= "center")
    	bubbleUbicacionActual.add_widget(labelUbicacionActual)
    	mapmarkerpopupUbicacionActual.add_widget(bubbleUbicacionActual) #creo un marcador con etique para saber la ubicacion actual, es de color rojo
    	"""

    	#self.ids.mapview.center_on(4.795100942698568, -75.6890602859938) #Me centra en la utp.
    	if len(self.listaMarker)>0:
    	    for marker in range(len(self.listaMarker)):
    	        self.ids.mapview.remove_widget(self.listaMarker[marker])
    	    self.listaMarker=[] #La reseteo para poder meter los mapMarker de los vehiculos actualizados.

    	#Se hace la consulta a la BD para obtener las lat y lon de los vehiculos-----------------------BD
    	#self.listaMarker.append(mapmarkerpopupUbicacionActual)

    	#hacer consulta base de datos
    	pos = UbicacionVehiculo.obtenerData(UbicacionVehiculo)


    	for e in pos:
    	    mapmarkerpopup=MapMarkerPopup(lat=float(e[1]), lon=float(e[2]), color=(0,1,1,1), popup_size= (120,70)) #acepta 1,0,1,1 o 0,0,0,1 o 0,1,1,1
    	    bubble=Bubble()
    	    label= Label(text= "[b]" + Vehiculo.getNamevehiculo(Vehiculo, e[0]) +  "[/b]", markup= True, halign= "center")
    	    bubble.add_widget(label)
    	    mapmarkerpopup.add_widget(bubble)
    	    self.listaMarker.append(mapmarkerpopup)

    	for i in range(len(pos)):
    	    self.ids.mapview.add_widget(self.listaMarker[i])

    def lugaresParaUbicacionActual(self): #Los lugares cercanos a mi ubicacion actual me los muestra.
        pass
        """
        for marker in range(len(self.listaMarker)):
    		self.ids.mapview.remove_widget(self.listaMarker[marker])
    	self.listaMarker=[]
    	CLIENT_ID = '' # your Foursquare ID
    	CLIENT_SECRET = '' # your Foursquare Secret
    	VERSION = '20190717'
    	LIMIT = 50
    	neighborhood_latitude=self.latitudActual
    	neighborhood_longitude=self.longitudActual
    	radius = 500
    	url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, VERSION, neighborhood_latitude, neighborhood_longitude,radius,LIMIT)
    	results = requests.get(url).json()
    	lugares = results['response']['groups'][0]['items']
    	lugaresCercanos = json_normalize(lugares)

    	filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
    	lugaresCercanos =lugaresCercanos.loc[:, filtered_columns]
    	# filter the category for each row
    	lugaresCercanos['venue.categories'] = lugaresCercanos.apply(lambda categorias: categorias , axis=1)
    	# clean columns
    	lugaresCercanos.columns = [col.split(".")[-1] for col in lugaresCercanos.columns]

    	self.ids.mapview.center_on(self.latitudActual, self.longitudActual) #mapa centrado en ubicacion actual
    	self.ids.mapview.zoom=17

    	mapmarkerpopupUbicacionActual=MapMarkerPopup(lat= self.latitudActual,lon= self.longitudActual, popup_size= (120,70), color=(0,0,0,1))
    	bubbleUbicacionActual=Bubble()
    	labelUbicacionActual= Label(text= "[b]Ubicaion actual![/b]", markup= True, halign= "center")
    	bubbleUbicacionActual.add_widget(labelUbicacionActual)
    	mapmarkerpopupUbicacionActual.add_widget(bubbleUbicacionActual)
    	self.listaMarker.append(mapmarkerpopupUbicacionActual)
    	#El for es para obtener la ubicacion de los lugares cercanos que necesito, y poner los marcadores
    	for lat, lng, categoria in zip(lugaresCercanos.lat, lugaresCercanos.lng, lugaresCercanos.categories):
    		mapmarkerpopup=MapMarkerPopup(lat=lat, lon=lng, color=(1,0,1,1), popup_size= (300,70))
    		bubble=Bubble()
    		label= Label(text= categoria, halign= "center")
    		bubble.add_widget(label)
    		mapmarkerpopup.add_widget(bubble)
    		self.listaMarker.append(mapmarkerpopup)

    	for i in range(len(self.listaMarker)):
    		self.ids.mapview.add_widget(self.listaMarker[i])
        """
