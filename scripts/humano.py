#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Humano(): # Creamos la clase Humano

    def __init__(self, edad:int, nombre:str, longitud:int): # Definimos el atributo edad y nombre
        '''Inicializador de la clase '''
        self.edad = edad # Definimos que el atributo edad
        self.nombre = nombre # Definimos que el atributo nombre
        self.cabello_longitud = longitud

    def peluquear(self, cant:int):
        '''método para reducir el cabello en una cantidad 
        Requiere la cantidad'''
        self.cabello_longitud=self.cabello_longitud-cant
        return self.cabello_longitud

    def get_name(self):
        return self.get_name
    
    def get_age(self):
        return self.get_name


pedro = Humano(31, "Pedro", 10) # Instancia

pedro.get_name()
pedro.nombre

// "Pedro"

pedro.get_age()
pedro.edad

// 31

pedro.peluquear(5)

// 5


pedro.__new__ -> constructor
pedro.
