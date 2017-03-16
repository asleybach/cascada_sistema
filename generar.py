#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.0.1')
import os
import sys
from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')
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

class Operaciones_Especiales(App):
	def build(self):
		
		pantalla=GridLayout(orientation = 'horizontal',rows=2,spacing=1, padding=1)			
		marco_imagen=BoxLayout(orientation = 'vertical', spacing=1, padding=1)
		filename = join(kivy.kivy_data_dir, 'logo', 'kivy-icon-64.png')
		imagen= Image(source=filename)
		label1=Label(text='Sistema Administrativo Conjunto Residencial La Cascada', font_size=20)
		label2=Label(text='Disponible desde marzo 2017 v1.0')
		label3=Label(text='Servicio de Reportes y Otras Operaciones', font_size=14)
		marco_imagen.add_widget(imagen)
		marco_imagen.add_widget(label1)
		marco_imagen.add_widget(label2)
		marco_imagen.add_widget(label3)
		caja=GridLayout(orientation = 'vertical',rows=3,spacing=5, padding=5,cols=2)
		boton1=Button(text='Crear Año de Mensualidades',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton2=Button(text='Crear Cuota Especial',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton3=Button(text='Reporte de Mensualidades Por año/mes',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton4=Button(text='Crear Informe Cuota Especial',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton5=Button(text='Editar Propietarios',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		boton6=Button(text='Salir de Operaciones Especiales',size_hint=(.3,.3),background_color=(0, 0, 1.5, 2.5))
		label_ingreso=Label(text="")			
		caja.add_widget(boton1)
		caja.add_widget(boton2)
		caja.add_widget(boton3)
		caja.add_widget(boton4)
		caja.add_widget(boton5)
		caja.add_widget(boton6)	
				
		pantalla.add_widget(marco_imagen)
		pantalla.add_widget(caja)
		
		def salir(self):			
			Operaciones_Especiales().stop()
		boton6.bind(on_press=salir)	
		
		def mensualidad_nueva(self):
			os.system("/usr/bin/python posmes.py")
			return
		boton1.bind(on_release=mensualidad_nueva)
		
		def cuota_especiales(self):
			os.system("/usr/bin/python posespecial.py")
		boton2.bind(on_release=cuota_especiales)
		
		def Editar_Propietarios(self):
			os.system("/usr/bin/python Editar_Propietarios.py")
		boton5.bind(on_release=Editar_Propietarios)
		
		
		
		return pantalla
		
		
Operaciones_Especiales().run()
