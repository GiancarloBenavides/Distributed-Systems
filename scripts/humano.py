#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Humano():
    """ Creamos la clase Humano. """

    def __init__(self, nombre: str, apellido: str, edad: int, longitud_cabello: int) -> None:
        """Inicializa los atributos de la clase."""
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.longitud_cabello = longitud_cabello

    def cortar_cabello(self, cantidad: int = 2) -> int:
        """ Corta el cabello de un humano en una cantidad. \n
        \n    Args:\n    -------\n
        * cantidad (int): \n\n
        \n    Returns:\n    -------\n
                Int
        """

        if self.longitud_cabello > cantidad:
            self.longitud_cabello -= cantidad
        return self.longitud_cabello

    # Getters
    def get_name(self) -> str:
        return self.get_name

    def get_age(self) -> int:
        return self.get_name

    # Setters
    def set_name(self, name: str) -> int:
        self.get_name = name
