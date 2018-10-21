import categoria_nombre
import categoria_apellido
import categoria_ciudad
import categoria_fruta
import categoria_color

# Clase que define todos los componentes del juego
# como lo son los jugadores, la configuracion (diccionario con todas las palabras de todas las categorias del jeugo)
class Stop:
  __categorias__ = {}
  __letra_de_juego__ = ""
  __jugadores__ = []

  def __init__(self, jugadores, elementos_categorias, letra_de_juego):
    self.__categorias__ = {
      "categoria_nombre": categoria_nombre.CategoriaNombre(elementos_categorias["nombres"]),
      "categoria_apellido": categoria_apellido.CategoriaApellido(elementos_categorias["apellidos"]),
      "categoria_ciudad": categoria_ciudad.CategoriaCiudad(elementos_categorias["ciudades"]),
      "categoria_fruta": categoria_fruta.CategoriaFruta(elementos_categorias["frutas"]),
      "categoria_color": categoria_color.CategoriaColor(elementos_categorias["colores"])
    }
    self.__letra_de_juego__ = letra_de_juego
    self.__jugadores__ = jugadores

  # Metodo que retorna la letra con la que se esta jugando
  def get_letra_de_juego(self):
    return self.__letra_de_juego__

  # Metodo que retorna una la instancia de la categoria de nombres
  def get_categoria(self, nombre_categoria):
    return self.__categorias__[nombre_categoria]

  def get_categorias(self):
    return self.__categorias__.keys()

  # Metodo que calcula(computa) los puntos de los jugadores para una determinada categoria 
  def computar(self):
    for categoria in self.get_categorias():
      diccionario_respuestas = {}
      for jugador in self.__jugadores__:
        # Revisa si la respues del jugador actual existe en el diccionario de respuestas
        termino = jugador.get_respuestas()[categoria]

        # Revisa si ese termino, es valido para categoria
        if self.get_categoria(categoria).buscar_elemento(termino, self.__letra_de_juego__):
          pass
        else:
          # Si el termino a computar, no es valido (no existe o no aplica), no se tiene en cuenta en el computo
          continue
        if termino in diccionario_respuestas:
          # si esta, suma 1 al total y agrega dicho jugador a esa respuesta
          diccionario_respuestas[termino]["cantidad"] =  diccionario_respuestas[termino]["cantidad"] + 1
          diccionario_respuestas[termino]["jugadores"].append(jugador)
        else:
          # significa que esa respuesta es nueva, por lo tanto se agrega al diccionario de respuestas, con el jugador que la digito
          diccionario_respuestas[termino] = {"cantidad": 1, "jugadores": [jugador]}
      
      # Ahora por aca termino en el diccionario de palabras, entrego la puntuacion
      for termino in diccionario_respuestas.keys():
        # Divido el maximo de puntos de un termino, entre el numero de jugadores que lo escribieron
        puntos_por_jugador = 100 / diccionario_respuestas[termino]["cantidad"]
        # A cada jugador que escribio dicho termino, le asigno su parte de la puntuacion
        for jugador in diccionario_respuestas[termino]["jugadores"]:
          jugador.agregar_puntos(puntos_por_jugador)
  
  def mostrar_puntuacion(self):
    for jugador in self.__jugadores__:
      print("%s, terminaste con: %i puntos!" % (jugador.get_nombre(), jugador.get_puntos()))
          


