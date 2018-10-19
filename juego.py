# -*- coding: utf-8 -*-
"""
Creado 28 de Septiembre 08:06 p.m 

Autor : Manuel Sebastian Bautista Chavarro 
"""

import time
from jugador import Jugador
import stop

# diccionario de configuracion
# Aca se definene todas las palabras que van a ser analizadas por aca una de las categorias
configuracion = {
  "nombres": ["ana", "alana", "angelica", "anyela"],
  "apellidos": [],
  "ciudades": [],
  "frutas": [],
  "colores": []
  # todas las categorias que se requieran configurar....
}

nombre_jugador1 = input("Hola! jugador #1, porfavor escribe tu nombre: ")
jugador1 = Jugador(nombre_jugador1, 0)

letra_a_jugar = input("Bueno %s, cual es la letra con la que jugaremos? " % nombre_jugador1)

# Se inicia el juego, pasando los jugadores, la letra a jugar, y la configuracion de este
juego = stop.Stop(jugador1, "", configuracion, letra_a_jugar)

print("Inicia el juego!")
for categoria in ["categoria_nombre", "categoria_apellido", "categoria_ciudad", "categoria_fruta", "categoria_color"]:
  categoria_actual = juego.get_categoria(categoria)
  respuesta = categoria_actual.realizar_pregunta(nombre_jugador1, letra_a_jugar)
  # revisa si la respuesta digitada por el jugador es correcta
  if categoria_actual.buscar_elemento(respuesta):
    print("Jugador1, felicitaciones!, tienes 100 puntos")
  else:
    print("Jugador1, no acertaste!, tienes 0 puntos")

# en construccion :)