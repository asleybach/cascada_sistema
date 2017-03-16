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
print("Open DataBase in Operaciones_Especiales")
import kivy
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')
from kivy.core.window import Window
Window.clearcolor = (0,0,0.3,0)
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from os.path import join

class Editar_Propietarios(App):
	def build(self):
		boxlayout=BoxLayout(orientation='vertical',spacing=2,padding=5)
		
		titulo=BoxLayout(orientation='vertical')
		label2=Label(text='N° de Casa: ', font_size=16)
		textinput_casa=TextInput(multiline=False,font_size=16)
		titulo.add_widget(label2)
		titulo.add_widget(textinput_casa)		
				
		botones=BoxLayout(orientation='horizontal')
		enviar=Button(text='Buscar Propietario',background_color=(0, 0, 1.5, 2.5))
		#salir=Button(text='Salir',background_color=(0, 0, 1.5, 2.5))
		botones.add_widget(enviar)
		#botones.add_widget(salir)
		titulo.add_widget(botones)
		boxlayout.add_widget(titulo)
				
		cambio=GridLayout(orientation='horizontal',cols=2,rows=3)
		labeltitulo=Label(text="Nombre del Propietario:")
		labelshow=Label(text="")
		labelparacambio=Label(text="Cambiar Por: ")
		textIncambio=TextInput(multiline=False,font_size=16)
		botonsi=Button(text="Cambiar",background_color=(0, 0, 1.5, 2.5))
		botonno=Button(text="Cancelar Cambio",background_color=(0, 0, 1.5, 2.5))
		boxlayout.add_widget(cambio)
		
		
		
		def aceptar(self):
			cambio.add_widget(labeltitulo)
			cambio.add_widget(labelshow)
			cambio.add_widget(labelparacambio)
			cambio.add_widget(textIncambio)
			cambio.add_widget(botonsi)
			cambio.add_widget(botonno)
			casa=textinput_casa.text		
			cursor.execute("SELECT nombre_apellido from datos WHERE ID = {} ".format(casa))
			for raw in cursor:
				name=raw[0]
				if name==None:
					labelshow.text="Vacio"
				else:
					labelshow.text=raw[0]
			
			def cancelar_cambio(self):
				cnn_db.close()
				Editar_Propietarios().stop()
				return
			botonno.bind(on_press=cancelar_cambio)
			
			def cambiar(Button):
				casa=textinput_casa.text				
				nombrenuevo=textIncambio.text				
				cursor.execute("SELECT nombre_apellido from datos WHERE ID = {} ".format(casa))
				for raw in cursor:
					cursor.execute(" UPDATE datos SET nombre_apellido = '" + nombrenuevo + "' WHERE rowid= '" + casa + "' ")
					cnn_db.commit()
					print ("Editado Propietario")
				Editar_Propietarios().stop()			
																
			botonsi.bind(on_release=cambiar)			
		enviar.bind(on_release=aceptar)		
	
		return boxlayout
		
Editar_Propietarios().run()
