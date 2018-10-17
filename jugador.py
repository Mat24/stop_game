"""
    Clase de un jugador
    Define el "molde" de un judador, es decir las propiedades que identifican a un jugador.
    es decir:
    - nombre: cada jugador se identifica por un nombre
    - puntos: cada jugador lleva la "contabilizacion" de sus puntos (por defecto son cero)
"""

class Jugador:
    __nombre__ = ""
    __puntos__ = 0

    def __init__(self, nombre, puntos):
        self.__nombre__ = nombre
        self.__puntos__ = puntos

    def agregar_puntos(self, cantidad_puntos):
        self.__puntos__ = self.__puntos__ + cantidad_puntos