from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.garden.mapview import MapSource

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

root = Builder.load_string("""

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

			        MapMarker:
			            lat: 4.5330700
			            lon: -75.7043800

			        MapMarker:
			            lat: 3.4384
			            lon: -76.5232

			    Toolbar:
			        top: root.top
			        Button:
			            text: "Move to Lille, France"
			            on_release: mapview.center_on(50.6394, 3.057)
			        Button:
			            text: "Move to Sydney, Autralia"
			            on_release: mapview.center_on(-33.867, 151.206)

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
	pass
