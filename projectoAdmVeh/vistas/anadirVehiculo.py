from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


#import to negocio
from negocio.tipoVehiculo import TipoVehiculo
from negocio.marcaVehiculo import MarcaVehiculo
from negocio.lineaVehiculo import LineaVehiculo

class AgregarVehiculo(Screen):
	def __init__(self, **kwargs):
		self.register_event_type('on_guardar')
		super(AgregarVehiculo, self).__init__(**kwargs)
		Clock.schedule_once(self.valoresSpinner)


		#cargo los tipo de vehiculos
		self.tipos = TipoVehiculo.getAllTipos(TipoVehiculo)
		self.marcas = []
		self.lineas = []


		#Guardo la referencia de los valores escogidos
		self.tipoSelect = None
		self.marcaSelect = None
		self.lineaSelect = None
		

	def valoresSpinner(self,dt):
		#consulta para traer los vehiculos y anexar en esta lista
		self.ids.spinner_1.values=[tipo.tipo for tipo in self.tipos]

	def marcasDeTipoVehiculo(self):


		self.ids.spinner_2.text="Seleccione la marca"
		print("cargando marcas de vehiculo",self.ids.spinner_1.text)
		self.tipoSelect = TipoVehiculo.selectTipo(TipoVehiculo, self.ids.spinner_1.text, self.tipos)
		print("seleccionando tipo",self.tipoSelect)

		self.marcas = MarcaVehiculo.getAllMarcas(MarcaVehiculo,self.tipoSelect)
		
		self.ids.spinner_2.values=[m.marca for m in self.marcas]

		
		

	def modelosDeMarcaVehiculo(self):
		self.ids.spinner_3.text = "seleccione linea"
		self.marcaSelect = MarcaVehiculo.selectMarca(MarcaVehiculo,self.ids.spinner_2.text, self.marcas)

		self.lineas = LineaVehiculo.getAllLineas(LineaVehiculo, self.marcaSelect)


		self.ids.spinner_3.values = [l.linea for l in self.lineas]

	def on_guardar(self, *args):
		
		#armar el vehiculo para guardarlo a la base de datos

		
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
			self.lineaSelect = LineaVehiculo.selectLinea(LineaVehiculo,self.ids.spinner_3.text, self.lineas)
			#esto seme esta ejecutando dos veces
			#print("linea seleccionada", self.lineaSelect)
			#agregar a db el vehiculo
			return [True, nombreVehiculo] 