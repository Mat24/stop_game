# -*- coding: utf-8 -*-
"""
Creado 28 de Septiembre 08:06 p.m 

Autor : Manuel Sebastian Bautista Chavarro 
"""

import time
from jugador import Jugador
from stop import Stop

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

total_jugadores = int(input("Hola! en el dia de hoy cuantas personas jugaremos? (numero de jugadores?):"))
numero_jugador = 1
jugadores = []
while numero_jugador <= total_jugadores:
  nombre_jugador = input("Hola! jugador #%i, porfavor escribe tu nombre: " % numero_jugador)
  jugadores.append(Jugador(nombre_jugador, 0))
  print("%s, bienvenido al juego!" % nombre_jugador)
  numero_jugador += 1

letra_a_jugar = input("Bueno %s, cual es la letra con la que jugaremos? " % jugadores[0].get_nombre())

# Para evitar que entre los jugadores se copien las respuestas, hacemos uso de getpass, que oculta lo escrito por la terminal
print("ADVERTENCIA!: debido a cuestiones de seguridad, las respuestas de cada jugador no seran visibles a medida que se escriben")
print("asi que no te precupes si a medida que escribes no ves nada, asegurate de escribir bien tu respuesta, cuando la tengas, solo presiona ENTER!")
time.sleep(2)
# Se inicia el juego, pasando los jugadores, la letra a jugar, y la configuracion de este
juego = Stop(jugadores, configuracion, letra_a_jugar)

print("Inicia el juego!")
for categoria in juego.get_categorias():
  categoria_actual = juego.get_categoria(categoria)
  # Por cada jugador, hace la pregunta de la categoria correspondiente
  for jugador in jugadores:
    respuesta = categoria_actual.realizar_pregunta(jugador.get_nombre(), letra_a_jugar)
    jugador.agregar_respuesta(categoria, respuesta)
    # revisa si la respuesta digitada por el jugador es correcta
    if categoria_actual.buscar_elemento(respuesta, letra_a_jugar):
      print("%s, felicitaciones!, parece que tu respuesta tiene buena pinta" % jugador.get_nombre())
    else:
      print("%s, hmmm!, tu respuesta no me convence :(" % jugador.get_nombre())
# Aca se hace el calculo de todas las respuestas de todos los jugadores, y se distrubuyen los puntos.
juego.computar()

# Al final del juego, muestra la puntuacion de todos los jugadores
juego.mostrar_puntuacion()
