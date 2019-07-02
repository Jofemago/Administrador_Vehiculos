from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.lang import Builder

from db.creator import Creator



Builder.load_string("""
#Si meto el popup con todas las vistas, se duplica su contenido, poniendo el cod kv aca se soluciona ese inconveniente
<ConfirmPopup>: #Es para asegurar que sea el correo a guardar 
    cols:1
    Label:
        text: root.text # Obtiene el texto Desea guardar el correo
    GridLayout:
        cols: 2
        size_hint_y: None
        height: '44sp'
        Button:
            text: 'Si'
            on_release: root.dispatch('on_answer','si')
        Button:
            text: 'No'
            on_release: root.dispatch('on_answer', 'no')

"""
)

class ConfirmPopup(GridLayout): #Se crea el contenido para el popup de confirmacion
	text = StringProperty() #Segun entiendo, esto captura "Desea guardar el correo?"
	
	def __init__(self,**kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup,self).__init__(**kwargs)
		
	def on_answer(self, *args): #Me permite recibir la respuesta del dialogo, si o no
		pass 

class MainWindow(Screen): #Por el momento es la ventana inicial que es para agregar el correo, su contenido esta en el kv
	def __init__(self, **kwargs):
		super(MainWindow, self).__init__(**kwargs)
	def direccionadoBotonGuardarCorreo(self):
		informacionDelPopup="Desea guardar el correo?\n"+str(self.ids.correo.text)
		content = ConfirmPopup(text=informacionDelPopup) #Este texto que paso lo captura el stringProperty
		content.bind(on_answer=self._on_answer) #segun mi analisis, es para dar el mando de on_answer a _on_answer
		self.popup = Popup(title="Confirmacion",
							content=content,
							size_hint=(0.5, 0.5),
							auto_dismiss= False)
		self.popup.open()
		
	def _on_answer(self, instance, answer): #al oprimir el boton si o no se activa esta funcion
		self.popup.dismiss()
		if answer=='si':

			#write the mail in the config.json
			mail = str(self.ids.correo.text)
			creator = Creator()
			
			config = creator.makeConfigJSON()

			config["mail"] = mail
			config["mailvalidate"] = True

			creator.writeConfigJson(config)


			self.manager.current="segunda" #Cambio de ventana aqui porque depende de lo que seleccione en el popup si, no.
		elif answer=='no':
			pass