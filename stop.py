import categoria_nombre

# Clase que define todos los componentes del juego
# como lo son los jugadores, la configuracion (diccionario con todas las palabras de todas las categorias del jeugo)
class Stop:
  __categoria_nombre__ = None
  __letra_de_juego__ = ""

  def __init__(self, jugador1, jugador2, elementos_categorias, letra_de_juego):
    self.__categoria_nombre__ = categoria_nombre.CategoriaNombre(elementos_categorias["nombres"])
    self.__letra_de_juego__ = letra_de_juego

  # Metodo que retorna la letra con la que se esta jugando
  def get_letra_de_juego(self):
    return self.__letra_de_juego__

  # Metodo que retorna una la instancia de la categoria de nombres
  def get_categoria_nombres(self):
    return self.__categoria_nombre__