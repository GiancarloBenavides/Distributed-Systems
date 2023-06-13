#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Humano(): # Creamos la clase Humano

    def __init__(self, edad:int, nombre:str): # Definimos el atributo edad y nombre
        self.edad = edad # Definimos que el atributo edad
        self.nombre = nombre # Definimos que el atributo nombre

    def get_name(self):
        return self.get_name
    
    def get_age(self):
        return self.get_name


pedro = Humano(31, "Pedro") # Instancia

pedro.get_name()

// "Pedro"

pedro.get_age()

// "Pedro"