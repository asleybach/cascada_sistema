#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import sqlite3
sqlite3_file='cascada_propietarios'
cnn_db=sqlite3.connect(sqlite3_file)
cursor=cnn_db.cursor()
print("Start XD")
import kivy
kivy.require('1.0.1')
from kivy.config import Config
Config.set('graphics','fullscreen=auto')
from kivy.core.window import Window
Window.clearcolor = (0,0,0.3,0)
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from os.path import join
from kivy.animation import Animation
from kivy.clock import Clock

class main_app(App):
	def __init__(self, **kwargs):
		super(main_app, self).__init__(**kwargs)
			
	def build(self):		
		ventana=GridLayout(orientation = 'horizontal',rows=4,spacing=1, padding=1)		
		marco_imagen=BoxLayout(orientation = 'vertical', spacing=5, padding=5)		
		filename = join(kivy.kivy_data_dir, 'logo', 'kivy-icon-64.png')
		imagen= Image(source=filename)		
		
		label1=Label(text='Sistema Administrativo Conjunto Residencial La Cascada', font_size=20)
		label2=Label(text='Gestión Administrativa del Condominio de la Asociación', font_size=16)
		label3=Label(text='Disponible desde marzo 2017 v1.0')
		fotourbe= join('/home/roxy/proyectos/App/Cascada_Sistema/data/image/foto.jpg')
		imagen2=Image(source=fotourbe)
		marco_imagen.add_widget(imagen)
		marco_imagen.add_widget(label1)
		marco_imagen.add_widget(label2)
		marco_imagen.add_widget(label3)	
		marco2=BoxLayout(spacing=1, padding=1)
		marco2.add_widget(imagen2)
		
		marco_botones=BoxLayout(orientation='horizontal',cols=3,spacing=30, padding=1)
		boton1=Button(text='Control Mensualidad',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton2=Button(text='Operaciones Especiales',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton3=Button(text='Cerrar',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		marco_botones.add_widget(boton1)
		marco_botones.add_widget(boton2)
		marco_botones.add_widget(boton3)				
		ventana.add_widget(marco_imagen)
		ventana.add_widget(marco2)
		ventana.add_widget(marco_botones)		
		def cancel(self):
			cnn_db.close()
			print("close database..bye XD bye!!!")
			main_app().stop()
		boton3.bind(on_press=cancel)
		def Control_Mensualidad(self):
			os.system("/usr/bin/python control_mensualidad.py")
		boton1.bind(on_release=Control_Mensualidad)		
		def operaciones_especiales(self):
			os.system("/usr/bin/python generar.py")
		boton2.bind(on_release=operaciones_especiales)		
		return ventana
		
main_app().run()
