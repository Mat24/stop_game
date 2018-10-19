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

  def __init__(self, jugador1, jugador2, elementos_categorias, letra_de_juego):
    self.__categorias__ = {
      "categoria_nombre": categoria_nombre.CategoriaNombre(elementos_categorias["nombres"]),
      "categoria_apellido": categoria_apellido.CategoriaApellido(elementos_categorias["apellidos"]),
      "categoria_ciudad": categoria_ciudad.CategoriaCiudad(elementos_categorias["ciudades"]),
      "categoria_fruta": categoria_fruta.CategoriaFruta(elementos_categorias["frutas"]),
      "categoria_color": categoria_color.CategoriaColor(elementos_categorias["colores"])
    }
    self.__letra_de_juego__ = letra_de_juego

  # Metodo que retorna la letra con la que se esta jugando
  def get_letra_de_juego(self):
    return self.__letra_de_juego__

  # Metodo que retorna una la instancia de la categoria de nombres
  def get_categoria(self, nombre_categoria):
    return self.__categorias__[nombre_categoria]