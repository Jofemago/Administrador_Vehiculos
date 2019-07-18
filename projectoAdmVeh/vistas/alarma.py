from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
#from pygame import mixer

class Alarma(Screen):
	#l=[]
	def __init__(self, **kwargs):
		super(Alarma, self).__init__(**kwargs)
		self.name="alarma"
		#Clock.schedule_once(lambda dt:self.scrollVehiculos())

	def alarmaActivada(self, ventanaActual, nombreAlarma, recargaOmantenimiento): #para lanzar una alarma que se haya programado.
		#mixer.init()
		#mixer.music.load('helio.mp3')
		#mixer.music.play()
		contenedorBtn = GridLayout(cols=3, size_hint_y= None, height='44sp')
		contenedorGeneral=GridLayout(cols=1)
		informacionAlarma = Label(text="Usted ha programado la alarma: "+nombreAlarma+" para "+recargaOmantenimiento+" del vehiculo: no se")
		btnAceptar = Button(text="OK", on_press=lambda alarm:self.regresaraPestanaAnterior(ventanaActual))

		contenedorBtn.add_widget(BoxLayout())
		contenedorBtn.add_widget(btnAceptar)
		contenedorBtn.add_widget(BoxLayout())

		contenedorGeneral.add_widget(informacionAlarma)
		contenedorGeneral.add_widget(contenedorBtn)

		self.popup = Popup(title="ALARMA",content=contenedorGeneral,size_hint=(1, 1), auto_dismiss= False)
		self.popup.open()

	def regresaraPestanaAnterior(self, ventana):
		#os.close("helio.mp3")
		self.popup.dismiss()
		self.manager.current=ventana
