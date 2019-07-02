from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class AgregarVehiculo(Screen):
	def __init__(self, **kwargs):
		self.register_event_type('on_guardar')
		super(AgregarVehiculo, self).__init__(**kwargs)
		Clock.schedule_once(self.valoresSpinner)

	def valoresSpinner(self,dt):
		#consulta para traer los vehiculos y anexar en esta lista
		self.ids.spinner_1.values=['vehiculo1' , 'vehiculo2', 'vehiculo3']

	def marcasDeTipoVehiculo(self):
		self.ids.spinner_2.text="Seleccione la marca"
		if self.ids.spinner_1.text=="vehiculo1":
			self.ids.spinner_2.values=['marca1' , 'marca1', 'marca1']
		elif self.ids.spinner_1.text=="vehiculo2":
			self.ids.spinner_2.values=['marca2' , 'marca2', 'marca2']
		elif self.ids.spinner_1.text=="vehiculo3":
			self.ids.spinner_2.values=['marca3' , 'marca3', 'marca3']

	def modelosDeMarcaVehiculo(self):
		self.ids.spinner_3.values=['modelo1' , 'modelo2', 'modelo3']

	def on_guardar(self, *args):
		nombreVehiculo=self.ids.nombreVehiculo.text
		valorTacometro=self.ids.valorTacometro.text
		tipoCombustible=self.ids.spinner_0.text
		tipoVehiculo=self.ids.spinner_1.text
		marcaVehiculo=self.ids.spinner_2.text
		modeloVehiculo=self.ids.spinner_3.text
		if nombreVehiculo=="" or valorTacometro=="" or tipoCombustible=="Combustible" or tipoVehiculo=="Tipo vehiculo" or marcaVehiculo=="marca" or modeloVehiculo=="modelo":
			self.ids.advertenciaAgregarVehiculo.text="Complete todos los campos."
			return [False, None]
		else:
			#agregar a db
			return [True, nombreVehiculo] 