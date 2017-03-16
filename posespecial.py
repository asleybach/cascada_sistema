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
print("Open DataBase")
import kivy
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')
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

class mensualidades_especiales(App):
	def build(self):
		boxlayout=BoxLayout(orientation='vertical')
		label2=Label(text='Ingresa Nombre de la Mensualidad Especial:')
		textinput_name=TextInput(multiline=False,font_size=20)		
		botones=GridLayout(orientation='horizontal',cols=2)
		enviar=Button(text='Aceptar',background_color=(0, 0, 1.5, 2.5))
		salir=Button(text='Salir',background_color=(0, 0, 1.5, 2.5))
		botones.add_widget(enviar)
		botones.add_widget(salir)
		boxlayout.add_widget(label2)		
		boxlayout.add_widget(textinput_name)
		boxlayout.add_widget(botones)
		def cerrar(self):
			mensualidades_especiales().stop()
			cnn_db.close()
			return
		salir.bind(on_press=cerrar)
		
		def aceptar(self):
			nombre=textinput_name.text
			cursor.execute('''CREATE TABLE IF NOT EXISTS {} (pago NUMERIC)'''.format(nombre))
			i=1
			for i in range(136):
				cursor.execute('''INSERT INTO {} VALUES(NULL)'''.format(nombre))
				cnn_db.commit()
				print("Do register {} for {}".format(i,nombre))			
			cnn_db.close()
			print ("close DataBase")		
			mensualidades_especiales().stop()
		enviar.bind(on_press=aceptar)
		return boxlayout
		
mensualidades_especiales().run()
