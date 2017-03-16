#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.0.1')
import os
import sys
import sqlite3
sqlite3_file='cascada_propietarios'
cnn_db=sqlite3.connect(sqlite3_file)
cursor=cnn_db.cursor()
print("Open DataBase in Control_Mensualidad")
import kivy
from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')
from kivy.core.window import Window
Window.clearcolor = (0,0,0.3,0)
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from reportlab.lib import enums
class Control_Mensualidad(App):
	def __init__(self, **kwargs):
		super(Control_Mensualidad, self).__init__(**kwargs)		
	def build(self):		
		ventana=GridLayout(orientation = 'horizontal',rows=9,spacing=1, padding=1)		
		marco_input=BoxLayout(orientation='vertical')
		InCasa=TextInput(multiline=False, font_size=14,focus=True)
		label4=Label(text='N° de Casa: ', font_size=14)
		marco_salida=BoxLayout(orientation='vertical')
		label_salida_datos=Label(text="", font_size=14)
		label2_salida_datos=Label(text="", font_size=10)
		caja_adicional2016=BoxLayout(orientation='horizontal',spacing=1, padding=1)
		label3_salida_datos=Label(text="", font_size=10)
		caja_adicional2017_a=BoxLayout(orientation='horizontal',spacing=1, padding=1)
		caja_adicional2017_b=BoxLayout(orientation='horizontal',spacing=1, padding=1)	
		marco_input.add_widget(label4)
		marco_input.add_widget(InCasa)
		marco_salida.add_widget(label_salida_datos)
		marco_salida.add_widget(label2_salida_datos)
		marco_salida.add_widget(caja_adicional2016)
		marco_salida.add_widget(label3_salida_datos)	
		marco_salida.add_widget(caja_adicional2017_a)
		marco_salida.add_widget(caja_adicional2017_b)
		
		marco_cobro=GridLayout(orientation='horizontal',cols=2,rows=8,spacing=1, padding=1)
		labelmarco1=Label(text="Ingrese año de la cuota: ")
		Inyear=TextInput(multiline=False,font_size=8)
		labelmarco2=Label(text="Mes a pagar (en/dic): ")
		Inmes=TextInput(multiline=False,font_size=8)
		labelmarco3=Label(text="monto a cancelar: ")
		Inmonto=TextInput(multiline=False,font_size=8)
		labelmarco4=Label(text="forma de pago (efect/trans): ")
		Inpago=TextInput(multiline=False,font_size=8)
		boton=Button(text="Procesar Pago Y Facturar",background_color=(0, 0, 1.5, 2.5))
		labelstatus=Label(text="")
				
		marco_botones=BoxLayout(orientation='horizontal',spacing=10, padding=1)
		boton1=Button(text='Buscar',size_hint=(.3,.2),background_color=(0, 0, 1.5, 2.5))
		boton2=Button(text='Limpiar',size_hint=(.3,.2),background_color=(0, 0, 1.5, 2.5))
		boton4=Button(text='Cerrar',size_hint=(.3,.2),background_color=(0, 0, 1.5, 2.5))
		marco_botones.add_widget(boton2)
		marco_botones.add_widget(boton1)
		marco_botones.add_widget(boton4)		
		ventana.add_widget(marco_input)		
		ventana.add_widget(marco_salida)
		ventana.add_widget(marco_cobro)
		ventana.add_widget(marco_botones)
		
						
		def buscar(text):
			a=str(InCasa.text)
			if a=="":
				texto_error='''
\nChequee el dato n° de casa en campo correspondiente\nPosiblemente este vacio...\n\n\n\nclic fuera de este mensaje para volver'''
				popup = Popup(title='Casilla Vacia...Chequee por favor ', content=Label(text=texto_error),
				size_hint=(None, None), size=(400,350))
				popup.open()
			else:
				cursor.execute('''SELECT nombre_apellido from datos WHERE ID = {} '''.format(a))
				cnn_db.commit()
				for raw in cursor:
						name=raw[0]
						if name == None:
							name='None'
					 	label_salida_datos.text = ("Nombre y Apellido del Propietario : " + name + " ")
						label2_salida_datos.text=("Status de las Mensualidades 2016")						
						meses2016=('mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
						mesesa=('enero','febrero','marzo','abril','mayo','junio')
						mesesb=('julio','agosto','septiembre','octubre','noviembre','diciembre')
						for i in meses2016:													
							cursor.execute('''SELECT {} from a2016 WHERE rowid = {} '''.format(i,a))
							cnn_db.commit()
							for raw in cursor:
								if (raw[0] ==None) or (raw[0]=="") or (raw[0]==0):
									caja_adicional2016.add_widget(Button(background_color=(1.5, 0, 0, 1.5),text='{}'.format(i)))									
								else:
									caja_adicional2016.add_widget(Button(background_color=(0,1.5, 0, 1.5),text='{}'.format(i)))
						label3_salida_datos.text=("Status de las Mensualidades 2017")
						for i in mesesa:													
							cursor.execute('''SELECT {} from a2017 WHERE rowid = {} '''.format(i,a))
							cnn_db.commit()
							for raw in cursor:
								if (raw[0] ==None) or (raw[0]=="") or (raw[0]==0):
									caja_adicional2017_a.add_widget(Button(background_color=(1.5, 0, 0, 1.5),text='{}'.format(i)))
									
								else:
									caja_adicional2017_a.add_widget(Button(background_color=(0,1.5, 0, 1.5),text='{}'.format(i)))
						for i in mesesb:												
							cursor.execute('''SELECT {} from a2017 WHERE rowid = {} '''.format(i,a))
							cnn_db.commit()
							for raw in cursor:
								if (raw[0] ==None) or (raw[0]==""):
									caja_adicional2017_b.add_widget(Button(background_color=(1.5, 0, 0, 1.5),text='{}'.format(i)))
								else:
									caja_adicional2017_b.add_widget(Button(background_color=(0,1.5, 0, 1.5),text='{}'.format(i)))							
		
				marco_cobro.add_widget(labelmarco1)
				marco_cobro.add_widget(Inyear)
				marco_cobro.add_widget(labelmarco2)
				marco_cobro.add_widget(Inmes)
				marco_cobro.add_widget(labelmarco3)
				marco_cobro.add_widget(Inmonto)
				marco_cobro.add_widget(labelmarco4)
				marco_cobro.add_widget(Inpago)
				marco_cobro.add_widget(boton)
				marco_cobro.add_widget(labelstatus)
			
			
				def procesar(Button):					
					year=str(Inyear.text)
					a=str(InCasa.text)
					pago=Inmes.text
					costo=Inmonto.text
					tipo=Inpago.text
					cursor.execute("SELECT {} from a{} WHERE rowid = {} ".format(pago,year,a))			
					for raw in cursor:
						if (raw[0] == None) or (raw[0] == "") or (raw[0]==0):
							cursor.execute("UPDATE a{} SET {} = {} WHERE rowid= {}".format(year,pago,costo,a))
							labelstatus.text=("cancelada la cuota {} {}".format(pago,year))
							cnn_db.commit()
							styleSheet= getSampleStyleSheet()
							story=[]
							h1=styleSheet['Heading1']
							h1.pageBreakBefore=0
							h1.keepWithNext=1
							h1.alignment=1
							h1.backColor=colors.blue
							h2=styleSheet['Heading2']
							h2.pageBreakBefore=0
							h2.keepWithNext=1
							h2.alignment=1
							style=styleSheet['Normal']
							style.alignment=1
							style.setFont=('Tahoma',14)
							style.pageBreakBefore=0
							style.keepWithNext=1
							P=Paragraph("  . . .  ",h1)
							story.append(P)
							P=Paragraph("Conjunto Residencial La Cascada",style)
							story.append(P)
							style2=styleSheet['Normal']
							style.alignment=0
							style2.pageBreakBefore=0
							style2.keepWithNext=1
							P=Paragraph("Avenida Aragua, Sector La Morita",style)
							story.append(P)
							P=Paragraph("Municipio Santiago Mariño",style)
							story.append(P)
							P=Paragraph("Rif: ",style)
							story.append(P)
							texto=('''<b>Facturación de Cuota Mensual de Condominio</b>''') 
							P=Paragraph(texto,h2)
							story.append(P)
							texto=('''<b>Original-Vecino</b>''') 
							P=Paragraph(texto,style2)
							story.append(P)
							P=Paragraph("<i>Datos del Propietario: </i><b>"+ name + "</b>",style)
							story.append(P)
							P=Paragraph("<i>N° de Casa: </i> <b>{}</b>".format(a),style)
							story.append(P)
							P=Paragraph("Fecha: ",style)
							story.append(P)
							story.append(Spacer(0,12))
							t=Table([["Año",'Mes','Monto','Tipo de Pago'],['{}'.format(year),'{}'.format(pago),'{}'.format(costo),'{}'.format(tipo)]])
							story.append(t)
							story.append(Spacer(0,65))
							P=Paragraph("  . . .   ",h1)
							story.append(P)
							#para copia del condominio
							P=Paragraph("",h1)
							story.append(P)
							story.append(Spacer(0,65))
							P=Paragraph("  . . .   ",h1)
							story.append(P)
							P=Paragraph("Conjunto Residencial La Cascada",style)
							story.append(P)
							style2=styleSheet['Normal']
							style.alignment=0
							style2.pageBreakBefore=0
							style2.keepWithNext=1
							P=Paragraph("Avenida Aragua, Sector La Morita",style)
							story.append(P)
							P=Paragraph("Municipio Santiago Mariño",style)
							story.append(P)
							P=Paragraph("Rif: ",style)
							story.append(P)
							texto=('''<b>Facturación de Cuota Mensual de Condominio</b>''')
							P=Paragraph(texto,h2)
							story.append(P)
							texto=('''<b>Copia-Control en el Condominio</b>''')
							P=Paragraph(texto,style2)
							story.append(P)
							P=Paragraph("<i>Datos del Propietario: </i><b>" + name + "</b>",style)
							story.append(P)
							P=Paragraph("<i>N° de Casa: </i> <b>{}</b>".format(a),style)
							story.append(P)
							P=Paragraph("Fecha: ",style)
							story.append(P)
							story.append(Spacer(0,12))
							t=Table([["Año",'Mes','Monto','Tipo de Pago'],['{}'.format(year),'{}'.format(pago),'{}'.format(costo),'{}'.format(tipo)]])
							story.append(t)
							story.append(Spacer(0,25))
							P=Paragraph("  . . .   ",h1)
							story.append(P)
							doc=SimpleDocTemplate("factura.pdf",pagesize=letter,showBoundary=1)
							doc.build(story)
							
							os.popen("/usr/bin/evince-previewer factura.pdf")
						else:
							labelstatus.text="cuota ya cancelada previamente"
				
					Inmes.text=""
					Inmonto.text=""					
					Inpago.text=""
					Inyear.text=""
							
				boton.bind(on_release=procesar)		
		
		boton1.bind(on_press=buscar)		
		def limpiar(self):			
			InCasa.text=""
			label_salida_datos.text=""
			label2_salida_datos.text=""
			label3_salida_datos.text=""
			labelstatus.text=""
			caja_adicional2016.clear_widgets()
			caja_adicional2017_a.clear_widgets()
			caja_adicional2017_b.clear_widgets()
			marco_cobro.clear_widgets()			
		boton2.bind(on_release=limpiar)	
		
		def cancel(self):
			cnn_db.close()
			print ("Close DataBase since Control_Mensualidad")
			Control_Mensualidad().stop()			
		boton4.bind(on_press=cancel)	
					
		return ventana		
Control_Mensualidad().run()
