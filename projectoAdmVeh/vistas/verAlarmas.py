"""
Me baso en ventanaAdminVehic para hacer el scroll y demas cosas, seguramente alla se encuentran los comentarios con mas detalle.
"""

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen 
from kivy.clock import Clock

Builder.load_string(""" 
<VerAlarmas>:
	orientation: "vertical"
	BoxLayout:
		size_hint_y: 0.15
		Label:
			text: "Nombre de la Alarma"
		Label:
			text: "Fecha"
		Label:
			text: "Tipo alarma"
		Label:
			text: "# de dias"
		Label:
			text: "Eliminar"
	BoxLayout:
		ScrollView:
			GridLayout:
				id: contenedorAlarmas
                cols: 1
                size_hint_y: None #Si esto no se pone, el scroll no aparece.
                row_default_height: root.height*0.1
                height: self.minimum_height
	BoxLayout:
		size_hint_y: 0.15
		padding: 100,15,100,15
		Button:
			text: "OK"
			on_release: root.dispatch('on_quitarPopup')

<BotonEliminarAlarma>:
    on_press: root.eliminarAlarma()
""")

class BotonEliminarAlarma(Button):
	def eliminarAlarma(self):
		#Lo elimino de la lista de alarmas
		self.parent.parent.remove_widget(self.parent)
		#Lo elimino de la base de datos
		#print(self.id) #id es el nombre de la alarma el cual es unico, asi se puede eliminar de la bd

class VerAlarmas(BoxLayout):
	def __init__(self, **kwargs):
		self.register_event_type('on_quitarPopup') #cuando este evento ocurra, voy a enlazar on_quitarPopup con la f de la clase
												   #tableroPrincipal quitarPopupAlarmas para cerrar el popup.	
		super(VerAlarmas, self).__init__(**kwargs)
		Clock.schedule_once(lambda dt:self.listarAlarmas())

	def listarAlarmas(self):
		for i in range(10):
			self.ids.contenedorAlarmas.add_widget(BoxLayout(orientation="horizontal"))
		for i, n in enumerate(self.ids.contenedorAlarmas.children): 
			n.add_widget(Label(text="Nombre "+str(i)))                                     
			n.add_widget(Label(text="Fecha"+str(i)))
			n.add_widget(Label(text="R o M "+str(i)))
			n.add_widget(Label(text=str(i))) 
			n.add_widget(BotonEliminarAlarma(text="Eliminar"+str(i)))

	def on_quitarPopup(self): #Esta f se implementa en la f de tableroPrincipal quitPupAl
		pass