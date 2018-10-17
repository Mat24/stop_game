# -*- coding: utf-8 -*-
"""
Creado 28 de Septiembre 08:06 p.m 

Autor : Manuel Sebastian Bautista Chavarro 
"""

import time
import jugador
import stop

# diccionario de configuracion
# Aca se definene todas las palabras que van a ser analizadas por aca una de las categorias
configuracion = {
  "nombres": ["ana", "alana", "angelica", "anyela"],
  "cuidades": [],
  "colores": []
  # todas las categorias que se requieran configurar....
}

nombre_jugador1 = input("Hola! jugador #1, porfavor escribe tu nombre: ")
jugador1 = jugador.Jugador(nombre_jugador1, 0)

letra_a_jugar = input("Bueno, cual es la letra con la que jugaremos? ")

# Se inicia el juego, pasando los jugadores, la letra a jugar, y la configuracion de este
juego = stop.Stop(jugador1, "", configuracion, letra_a_jugar)

print("Inicia el juego!")
respuesta_nombre_jugador1 = input("Porfavor escribe un %s que inicie con la letra %s ! : " % (juego.get_categoria_nombres().get_nombre_categoria(), letra_a_jugar))

# revisa si la respuesta digitada por el jugador es correcta
if juego.get_categoria_nombres().buscar_elemento(respuesta_nombre_jugador1):
  print("Jugador1, felicitaciones!, tienes 100 puntos")
else:
  print("Jugador1, no acertaste!, tienes 0 puntos")

# en construccion :)