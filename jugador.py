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
    __respuestas__ = {}

    def __init__(self, nombre, puntos):
        self.__nombre__ = nombre
        self.__puntos__ = puntos
        self.__respuestas__ = {}

    def get_nombre(self):
        return self.__nombre__

    def get_puntos(self):
        return self.__puntos__

    def get_respuestas(self):
        return self.__respuestas__

    def agregar_respuesta(self, categoria, respuesta):
        self.__respuestas__[categoria] = respuesta

    def agregar_puntos(self, cantidad_puntos):
        self.__puntos__ = self.__puntos__ + cantidad_puntos