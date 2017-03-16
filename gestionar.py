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
'''print("Open DataBase since Generar")'''
import kivy
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '300')
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

class gestion_propietario(App):
	def build(self):
		boxlayout=BoxLayout(orientation='vertical')
		label=Label(text='Gestión de Mensualidad Del Propietario')
		meses=GridLayout(orientation='horizontal')
		botones=GridLayout(orientation='horizontal',cols=2)
		enviar=Button(text='Aceptar')
		salir=Button(text='Salir')
		botones.add_widget(enviar)
		botones.add_widget(salir)
		boxlayout.add_widget(label)
		boxlayout.add_widget(meses)
		boxlayout.add_widget(botones)
		def cerrar(self):
			posmes().stop()
			return
		salir.bind(on_press=cerrar)
		
		def aceptar(self):
			mes=textinput.text
			print mes
			posmes().stop()
		enviar.bind(on_press=aceptar)
		return boxlayout
		
gestion_propietario().run()
