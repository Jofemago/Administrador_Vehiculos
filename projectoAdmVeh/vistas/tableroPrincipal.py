from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.lang import Builder

import time
from datetime import datetime
from kivy.properties import StringProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from vistas.verAlarmas import VerAlarmas

#import from db
from db.creator import Creator

#import from negocio
from negocio.recarga import Recarga
from negocio.vehiculo import Vehiculo
from negocio.tacometro import Tacometro
from negocio.mantenimiento import Mantenimiento

Builder.load_string("""
#:import time time

<TableroPrincipal>:
    name: "tableroPrincipal"
    TabbedPanel:
        do_default_tab: False
        TabbedPanelItem:
            text: 'Recargas'
            BoxLayout:
                orientation:"vertical"
                BoxLayout:
                    size_hint_y: 0.1
                    Label:
                        id: datosIncompletosRecarga
                        text: ""
                        color: 1,0,0,1
                BoxLayout:
                    spacing:50
                    padding: 20,10,70,10
                    size_hint_y:0.3
                    BoxLayout:
                        orientation: "vertical"
                        GridLayout:
                            size_hint_y:0.2
                            cols: 2
                            spacing:20
                            Label:
                                text: "Precio pagado por combustible"
                            TextInput:
                                id: precioRecarga
                                multiline: False
                                input_filter: "float"
                            Label:
                                text: "Kilometros recorridos"
                            TextInput:
                                id: kilometrosRecarga
                                multiline: False
                                input_filter: "float"
                    BoxLayout:
                        size_hint_x:0.5
                        Button:
                            text:"Guardar"
                            on_release: root.agregarRecarga()
                BoxLayout:
                    size_hint_y: 0.1
                    Label:
                        text: "Fecha"
                        color: 1,1,0,1
                    Label:
                        text: "Precio"
                        color: 1,0,1,1
                    Label:
                        text: "Kilometros Recorridos"
                        color: 0,0,1,1
                    Label:
                        text: "vehiculo"
                        color: 0,1,0,1
                ScrollView:
                    GridLayout:
                        id:contenedorRecargas
                        cols:1
                        size_hint_y: None #Si esto no se pone, el scroll no aparece.
                        row_default_height: root.height*0.1
                        height: self.minimum_height
                BoxLayout:
                    size_hint_y: 0.1
                    BoxLayout:
                    Button:
                        text: "Regresar"
                        on_press:
                            root.manager.current = "segunda"
                    BoxLayout


        TabbedPanelItem:
            text: 'Mantenimiento'
            on_release: root.confCorreo()
            BoxLayout:
                orientation:"vertical"
                BoxLayout:
                    padding: 10,20,10,20
                    spacing:20
                    size_hint_y:0.6
                    orientation: "vertical"
                    BoxLayout:
                        size_hint_y: 0.06
                        Label:
                            id: datosIncompletosMantenimiento
                            text: ""
                            color: 1,0,0,1
                    BoxLayout:
                        TextInput:
                            id:descripcionMantenimiento
                            hint_text:"Descripcion del mantenimiento"
                    BoxLayout:
                        spacing:20
                        TextInput:
                            id: precioMantenimiento
                            hint_text:"Precio Mantenimiento"
                            input_filter: "float"
                            multiline:False
                        TextInput:
                            id:kilometrosMantenimiento
                            hint_text:"Kilometros"
                            input_filter: "float"
                            multiline:False
                        Button:
                            text: "Guardar"
                            on_release: root.agregarMantenimiento()
                    BoxLayout:
                        Label:
                            text: "Fecha"
                            color: 1,1,0,1
                        Label:
                            text: "Precio"
                            color: 0,1,1,1
                        Label:
                            text: "Kilometros"
                            color: 0,0,1,1
                        Label:
                            text: "Descripcion"
                            color: 0,1,0,1
                        Label:
                            text: "vehiculo"
                            color: 0,1,0,1
                ScrollView:
                    GridLayout:
                        id:contenedorMantenimientos
                        cols:1
                        size_hint_y: None #Si esto no se pone, el scroll no aparece.
                        row_default_height: root.height*0.1
                        height: self.minimum_height
                BoxLayout:
                    size_hint_y: 0.1
                    BoxLayout:
                    Button:
                        text: "Regresar"
                        on_press:
                            root.manager.current = "segunda"
                    BoxLayout
        TabbedPanelItem:
            text: 'Reportes'
            BoxLayout:
                spacing: 20
                orientation: "vertical"
                BoxLayout:
                    size_hint_y: 0.06
                    Label:
                        id: advertenciaResporte
                        text: ""
                        color: 1,0,0,1
                BoxLayout:
                    orientation:"vertical"
                    size_hint_y:0.5
                    BoxLayout: #Es para dejar un espacio arriba
                    Spinner:
                        id: tipoReporte
                        text: 'Tipo de reporte'
                        values: ('Reporte de mantenimiento', 'Reporte de recargas','Reportes de huella de carbono')
                        #size_hint: [0.3, None]
                        height: '32dp'
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y:0.5
                    GridLayout:
                        cols: 2
                        spacing: 5
                        TextInput:
                            id: fechaInicial
                            hint_text: "Fecha inicial (dd/mm/aa)"
                            multiline: False
                        Button:
                            text: "Aceptar"
                            on_release: root.crearReporte()
                        TextInput:
                            id: fechaFinal
                            hint_text: "Fecha final (dd/mm/aa)"
                            multiline: False
                BoxLayout:
                    id: elegirListaReporte
                    orientation: "vertical"

                BoxLayout:
                    orientation: "vertical"
                    spacing: 4
                    size_hint_y:0.5
                    BoxLayout:
                        TextInput:
                            id: correopantalla
                            hint_text: ""
                            multiline: False
                    GridLayout:
                        cols:2
                        padding: 90,10
                        spacing: 20
                        Button:
                            text: "Aceptar"
                            on_press:
                                root.enviarReporte()
                        Button:
                            text: "Regresar"
                            on_press:
                                root.manager.current = "segunda"
        TabbedPanelItem:
            text: 'Alarmas'
            BoxLayout:
                orientation: "vertical"
                BoxLayout:
                    size_hint_y:0.3
                    Label:
                        id: hora
                        text: root.text
                    Label:
                        id:fecha
                        text: "Fecha: "+str(time.strftime("%d/%m/%Y"))
                BoxLayout:
                    size_hint_y:0.15
                    padding: 150,0,100,0
                    Label:
                        text: "Nombre de la alarma:"
                    TextInput:
                        id:nombre
                        multiline: False
                        hint_text:"Nombre diferente alarmas programada"
                GridLayout:
                    cols:1
                    GridLayout:
                        cols:8
                        BoxLayout:
                        BoxLayout:
                        CheckBox:
                            group: 'check'
                            id : recarga
                            text: "Recarga"
                        Label:
                            text: "Recarga"
                        CheckBox:
                            group: 'check'
                            id : mantenimiento
                            text: "Mantenimiento"
                        Label:
                            text: "Mantenimiento"
                        BoxLayout:
                        BoxLayout:
                    BoxLayout:
                        orientation:"vertical"
                        GridLayout:
                            cols:8
                            BoxLayout:
                            BoxLayout:
                            CheckBox:
                                group: 'check2'
                                id : fijo
                            Label:
                                text: "Fijo"
                            CheckBox:
                                group: 'check2'
                                id : periodico
                            Label:
                                text: "Periodico"
                            BoxLayout:
                            BoxLayout:
                        BoxLayout:
                            Label:
                                color: 1,0,0,1
                                id: mensajeVerificar
                GridLayout:
                    cols:2
                    spacing: 40
                    padding:50,10,30,20
                    Label:
                        text: "Numero de dias"
                    TextInput:
                        id: numeroDias
                        multiline: False
                        disabled: fijo.active
                        input_filter: "int"
                    Label:
                        text: "A partir de (dd/mm/aa):"
                    BoxLayout:
                        spacing: 40
                        BoxLayout:
                            size_hint_x:2
                            TextInput:
                                id: aPartirDe
                                multiline: False
                        BoxLayout:
                            Button:
                                text: "Agregar"
                                on_release: root.verificarDatosAlarmas(app)
                    Button:
                        text: "Ver alarmas"
                        on_release:
                            root.verAlarmas()

                    Button:
                        text: "Regresar"
                        on_press:
                            root.manager.current="segunda"
                            root.manager.transition.direction = "right"

"""
)

class TableroPrincipal(Screen):
    text = StringProperty() #Esto es para mantener listada la hora en la pestaña alarmas.
    instanciaVerAlarmas=[]
    def __init__(self,**kwargs):
        super(TableroPrincipal,self).__init__(**kwargs)
        self.text = str(time.strftime("%H:%M:%S"))
        Clock.schedule_interval(self.on_time,1) #hago esto para que se este actualizando el tiempo al crear alarmas.
        #Clock.schedule_once(lambda dt:self.listarRecargas())
        Clock.schedule_once(lambda dt:self.confCorreo())



    def confCorreo(self):

        c = Creator()
        filejson = c.makeConfigJSON()
        self.ids.correopantalla.text = filejson["mail"]


    #-----------------------------------PARA RECARGAS--------------------------------------------
    def listarRecargas(self):
        for i in range(3):
            self.ids.contenedorRecargas.add_widget(BoxLayout(orientation="horizontal"))
        for i, n in enumerate(self.ids.contenedorRecargas.children):
            n.add_widget(Label(text=str(time.strftime("%d/%m/%Y"))))
            n.add_widget(Label(text="Precio"+str(i)))
            n.add_widget(Label(text="Kilometros"+str(i)))

    def agregarRecarga(self):

        #obtener el nombre del vehiculo
        c = Creator()
        filejson = c.makeConfigJSON()
        nombreVehiculo = filejson["nameVehicule"]
        idVehiculo = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)

        if self.ids.precioRecarga.text=="" or self.ids.kilometrosRecarga.text=="":
            self.ids.datosIncompletosRecarga.text="Ingrese todos los datos"
        elif Tacometro.validarTacometro(Tacometro,int(self.ids.kilometrosRecarga.text), idVehiculo):
            self.ids.datosIncompletosRecarga.text="Esos kilometros ya fueron registrados debe ser superior"
        else:
            self.ids.datosIncompletosRecarga.text=""

            Recarga.makeRecarga(Recarga, nombreVehiculo,self.ids.precioRecarga.text, self.ids.kilometrosRecarga.text)

            box=BoxLayout(orientation="horizontal")
            box.add_widget(Label(text=str(time.strftime("%d/%m/%Y"))))
            box.add_widget(Label(text=self.ids.precioRecarga.text))
            box.add_widget(Label(text=self.ids.kilometrosRecarga.text))
            box.add_widget(Label(text=nombreVehiculo))
            self.ids.contenedorRecargas.add_widget(box)

    #-------------------------------------PARA MANTENIMIENTOS----------------------------------
    def listarMantenimientos(self):
        pass

    def agregarMantenimiento(self):

        c = Creator()
        filejson = c.makeConfigJSON()
        nombreVehiculo = filejson["nameVehicule"]
        idVehiculo = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)

        if self.ids.precioMantenimiento.text=="" or self.ids.kilometrosMantenimiento.text=="" or self.ids.descripcionMantenimiento.text=="":
            self.ids.datosIncompletosMantenimiento.text="Ingrese todos los datos"
        elif Tacometro.validarTacometro2(Tacometro,int(self.ids.kilometrosMantenimiento.text), idVehiculo):
            self.ids.datosIncompletosMantenimiento.text="Esos kilometros ya fueron registrados debe ser superior"
        else:

            km = self.ids.kilometrosMantenimiento.text
            descripcion = self.ids.descripcionMantenimiento.text
            precio = self.ids.precioMantenimiento.text
            Mantenimiento.makeMantenimiento(Mantenimiento,idVehiculo,descripcion, km, precio)

            self.ids.datosIncompletosMantenimiento.text=""
            box=BoxLayout(orientation="horizontal")
            box.add_widget(Label(text=str(time.strftime("%d/%m/%Y"))))
            box.add_widget(Label(text=self.ids.precioMantenimiento.text))
            box.add_widget(Label(text=self.ids.kilometrosMantenimiento.text))
            box.add_widget(Label(text=self.ids.descripcionMantenimiento.text))
            box.add_widget(Label(text=nombreVehiculo))
            self.ids.contenedorMantenimientos.add_widget(box)

    #-----------------------------------PARA CREAR UN REPORTE--------------------------------------
    def crearReporte(self):
        validarFecha=True
        fechai = 0
        fechaf = -1
        c = Creator()
        filejson = c.makeConfigJSON()
        nombreVehiculo = filejson["nameVehicule"]
        idVehiculo = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)
        try:
            fechai = datetime.strptime(self.ids.fechaInicial.text, "%d/%m/%Y").date()
            fechaf = datetime.strptime(self.ids.fechaFinal.text, "%d/%m/%Y").date()
        except:
            validarFecha=False #si la fecha esta mal
            print("entramos a la excepcion")
        if self.ids.tipoReporte.text=="Tipo de reporte" or self.ids.fechaInicial.text=="" or self.ids.fechaFinal.text=="":
            self.ids.advertenciaResporte.text="Complete todos los datos"
        elif fechai > fechaf:
            self.ids.advertenciaResporte.text="fechas invalidas"
        elif validarFecha:
            self.ids.advertenciaResporte.text=""
            print("Creando reporte")
            if self.ids.tipoReporte.text=="Reporte de recargas":
                self.ids.elegirListaReporte.clear_widgets() #Se elimina toda la lista del reporte elegido anteriormente
                nombreColumnas=BoxLayout(size_hint_y=0.1) #Box con los nombres de cada columna
                scrollReportes=ScrollView()
                gridReportes=GridLayout(cols=1, size_hint_y=None, row_default_height=self.height*0.1) #Va a contener todas las filas del repo
                gridReportes.bind(minimum_height=gridReportes.setter('height')) #es para que el scroll se pueda mover.
                columna= Label(text="Fecha Recarga", color=(1,1,0,1))
                nombreColumnas.add_widget(columna)
                columna= Label(text="Precio Recarga", color=(1,0,1,1))
                nombreColumnas.add_widget(columna)
                columna= Label(text="Kilometros Recorridos", color=(0,0,1,1))
                nombreColumnas.add_widget(columna)#;Recarga.getAllRecargas(Recarga, fechai, fechaf)
                rec = Recarga.getAllRecargas(Recarga, fechai, fechaf, idVehiculo)

                for i in range(len(rec)):
                    gridReportes.add_widget(BoxLayout(orientation="horizontal"))
                for i, n in enumerate(gridReportes.children):
                    print("")
                    n.add_widget(Label(text=  rec[i][2]))
                    n.add_widget(Label(text=  str(rec[i][1])))
                    n.add_widget(Label(text=  str(Tacometro.getValorTacByID(Tacometro,rec[i][3]))))
            elif self.ids.tipoReporte.text=="Reporte de mantenimiento":
                self.ids.elegirListaReporte.clear_widgets()
                nombreColumnas=BoxLayout(size_hint_y=0.1)
                scrollReportes=ScrollView()
                gridReportes=GridLayout(cols=1, size_hint_y=None, row_default_height=self.height*0.1)
                gridReportes.bind(minimum_height=gridReportes.setter('height')) #es para que el scroll se pueda mover.
                columna= Label(text="Fecha Mantenimiento", color=(1,1,0,1))
                nombreColumnas.add_widget(columna)
                columna= Label(text="Precio Mantenimiento", color=(1,0,1,1))
                nombreColumnas.add_widget(columna)
                columna= Label(text="Kilometros Recorridos", color=(0,0,1,1))
                nombreColumnas.add_widget(columna)

                mto = Mantenimiento.getAllMtos(Mantenimiento, fechai, fechaf,idVehiculo)
                for i in range(len(mto)):
                    gridReportes.add_widget(BoxLayout(orientation="horizontal"))
                for i, n in enumerate(gridReportes.children):
                    n.add_widget(Label(text= mto[i][3] ))
                    n.add_widget(Label(text= str(mto[i][1]) ))
                    n.add_widget(Label(text= str(Tacometro.getValorTacByID(Tacometro,mto[i][4] ))))
	        #Creo la lista de reportes para la huella de carbono----------->DB
            elif self.ids.tipoReporte.text=="Reportes de huella de carbono":
                self.ids.elegirListaReporte.clear_widgets()
                nombreColumnas=BoxLayout(size_hint_y=0.1)
                scrollReportes=ScrollView()
                gridReportes=GridLayout(cols=1, size_hint_y=None, row_default_height=self.height*0.1)
                gridReportes.bind(minimum_height=gridReportes.setter('height')) #es para que el scroll se pueda mover.
                columna= Label(text="Fecha Recarga Comb", color=(1,1,0,1))
                nombreColumnas.add_widget(columna)
                columna= Label(text="Cantidad combustible", color=(1,0,1,1))
                nombreColumnas.add_widget(columna)
                columna= Label(text="Huella Carbono (gr)", color=(0,0,1,1))
                nombreColumnas.add_widget(columna)
                for i in range(10):
                    gridReportes.add_widget(BoxLayout(orientation="horizontal"))
                for i, n in enumerate(gridReportes.children):
                    n.add_widget(Label(text=str(time.strftime("%d/%m/%Y"))))
                    n.add_widget(Label(text="cantidad"+str(i)))
                    n.add_widget(Label(text="huella"+str(i)))

            self.ids.elegirListaReporte.add_widget(nombreColumnas)
            scrollReportes.add_widget(gridReportes)
            self.ids.elegirListaReporte.add_widget(scrollReportes)

        else:
        	self.ids.advertenciaResporte.text="No ha ingresado una fecha correcta..."
        	validarFecha=True

    #------------------------------para mandar reportes-------------------
    def enviarReporte(self):

        c = Creator()
        filejson = c.makeConfigJSON()
        nombreVehiculo = filejson["nameVehicule"]
        idVehiculo = Vehiculo.getIdvehiculo(Vehiculo, nombreVehiculo)


        #self.ids.correopantalla.text = filejson["mail"]
        import csv
        import smtplib
        import mimetypes

        # Importamos los módulos necesarios
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.encoders import encode_base64

        fechai = 0
        fechaf = -1
        validarFecha = True
        try:
            fechai = datetime.strptime(self.ids.fechaInicial.text, "%d/%m/%Y").date()
            fechaf = datetime.strptime(self.ids.fechaFinal.text, "%d/%m/%Y").date()
        except:
            validarFecha=False #si la fecha esta mal
            print("entramos a la excepcion")

        if fechai > fechaf:
            self.ids.advertenciaResporte.text="fechas invalidas"
        elif validarFecha:
            self.ids.advertenciaResporte.text=""
            mto = Mantenimiento.getAllMtos(Mantenimiento, fechai, fechaf,idVehiculo)
            rec = Recarga.getAllRecargas(Recarga, fechai, fechaf, idVehiculo)
            f=open("reporteVehiculo.csv", "w")
            f.close()
            with open('reporteVehiculo.csv', 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Recargas del Vehiculo'])
                spamwriter.writerow(['Fecha', 'Precio', 'Kilometros recorridos'])
                for i in range(len(rec)):
                    #spamwriter.writerow(['Fecha'+str(i)]+ ['Precio'+str(i)]+ ['Kilometros recorridos'+str(i)])
                    spamwriter.writerow( [[rec[i][2] ] + [   str(rec[i][1]) ]  + [  str(Tacometro.getValorTacByID(Tacometro,rec[i][3])) ]])
                spamwriter.writerow(['Mantenimientos del Vehiculo'])
                spamwriter.writerow(['Fecha', 'Precio', 'Kilometros recorridos', 'Descripcion'])
                for i in range(len(mto)):
                    #spamwriter.writerow(['Fecha'+str(i)]+ ['Precio'+str(i)]+ ['Kilometros recorridos'+str(i)])
                    spamwriter.writerow([ [  mto[i][3] ] + [str(mto[i][1]) ] + [str(Tacometro.getValorTacByID(Tacometro,mto[i][4] )) ] + [mto[i][2] ]])


            # Creamos objeto Multipart, quien será el recipiente que enviaremos
            msg = MIMEMultipart()
            msg['From']="laboratoriodesw@gmail.com"
            msg['To'] = self.ids.correopantalla.text
            msg['Subject']="Reporte del vehiculo: " +  nombreVehiculo

            # Adjuntamos Imagen
            file = open("reporteVehiculo.csv", "r")
            attach_image = MIMEText(file.read())
            attach_image.add_header('Content-Disposition', 'attachment; filename = "reporteVehiculo.csv"')
            msg.attach(attach_image)

            # Autenticamos
            mailServer = smtplib.SMTP('smtp.gmail.com',587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login("laboratoriodesw@gmail.com","laboratoriodesw20191")

            # Enviamos
            mailServer.sendmail("laboratoriodesw@gmail.com", self.ids.correopantalla.text, msg.as_string())

            # Cerramos conexión
            mailServer.close()




    #-----------------------------------PARA VER ALARMAS--------------------------------------------

    def on_time(self,*args):
        self.text = "Hora: "+str(time.strftime("%H:%M:%S"))

    def verAlarmas(self): #Funcion que crea el popup para listar todas las alarmas.
        content=VerAlarmas()
        content.bind(on_quitarPopup=self.quitarPopupAlarmas)
        self.popup = Popup(title="ALARMAS PROGRAMADAS",
                            content=content,
                            size_hint=(1, 1),
                            auto_dismiss= False)
        self.popup.open()

    def quitarPopupAlarmas(self, instance):
        self.popup.dismiss()

    def verificarDatosAlarmas(self,app):
        #cadena solo es una prueba, la idea es que con nombreAlarma se compare los otros nombres de alam de la db para que no se repita.
        cadena="hola"
        hora=self.ids.hora.text
        fecha=self.ids.fecha.text
        nombreAlarma=self.ids.nombre.text
        numeroDias=self.ids.numeroDias.text
        aPartirDe=self.ids.aPartirDe.text
        recargaOmantenimiento=""
        fijoOperiodico=""
        vacioOno=False #me sirve para sabe si verificar el campo "numero de dias", esto depende de si selecciono fijo o periodico.
        insertarDatosBD=True
        #Decido cual chechbox se ha seleccionado
        if self.ids.mantenimiento.active:
            recargaOmantenimiento="Mantenimiento"
        elif self.ids.recarga.active:
            recargaOmantenimiento="Recarga"
        if self.ids.fijo.active:
            fijoOperiodico="Fijo"
            vacioOno=False
            numeroDias="" #No debe haber nada en numero de dias porque la recarga sera fija.
        elif self.ids.periodico.active:
            fijoOperiodico="Periodico"
            if numeroDias=="": #solo si esta activo periodico debo verificar que se ingrese algo en "a partir de."
                vacioOno=True
            else:
                vacioOno=False

        #Compruebo que el nombre de la alarma sea diferente a uno ya creado y que los campos esten todos digitados.
        if nombreAlarma==cadena:
            self.ids.mensajeVerificar.text="El nombre de la alarma ya existe, elija otro."
        elif hora=="" or fecha=="" or nombreAlarma=="" or aPartirDe=="" or vacioOno or nombreAlarma=="" or recargaOmantenimiento=="" or fijoOperiodico=="":
            self.ids.mensajeVerificar.text="Complete todos los datos"
        else:
            self.ids.mensajeVerificar.text=""
            try:
               datetime.strptime(aPartirDe, '%d/%m/%Y') #Verifico que la fecha sea correcta.
            except:
               self.ids.mensajeVerificar.text="No ha ingresado una fecha correcta..."
               insertarDatosBD=False #si la fecha esta mal, los datos no son insertados en DB
            #--------------------------------se crea la consulta para meter los siguientes datos a la db.--------------------------
            if insertarDatosBD:
                diaProgramado=aPartirDe[0]+aPartirDe[1]
                diaActual=fecha[7]+fecha[8]
                segundosLanzarAlarma=((int(diaProgramado)-int(diaActual))*24*60*60)+5 #Con respecto a la fecha actual
                #print(int(aPartirDe[0])-int(fecha[0]))
                Clock.schedule_once(lambda dt:self.sonarAlarma(app, nombreAlarma, recargaOmantenimiento),segundosLanzarAlarma)
                #print(hora,fecha,nombreAlarma,numeroDias,aPartirDe,recargaOmantenimiento,fijoOperiodico)

    def sonarAlarma(self, app, nombreAlarma, recargaOmantenimiento):
        ventanaActual=self.manager.current
        for ventana in app.root.screens:
            if ventana.name=="alarma":
                ventana.alarmaActivada(ventanaActual, nombreAlarma, recargaOmantenimiento)
        self.manager.current="alarma"
