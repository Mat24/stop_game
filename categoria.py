import getpass

class Categoria:
  __nombre__ = ""
  __elementos__ = []

  # Constructor de la clase, setea los parametros iniciales como lo es el nombre y la configuracion de la categoria.
  def __init__(self, nombre, elementos):
    self.__nombre__ = nombre
    self.__elementos__ = elementos

  # Retorna el nombre que se le ha configurado a una categoria.
  def get_nombre_categoria(self):
    return self.__nombre__

  # Retorna los elementos que se le han configurado a una categoria.
  def get_elementos(self):
    return self.__elementos__

  # Metodo que retorna verdadero si la primera letra de la respuesta, coincide con la letra que se esta jugando
  def coincide_letra(self, respuesta, letra_a_jugar):
    return respuesta[0] == letra_a_jugar

  # Busca un termino en una lista de elementos
  # Si lo encuentra, devuelve verdadero (True), de lo contrario, retornara falso (False)
  def buscar_elemento(self, termino, letra_a_jugar):
    if self.coincide_letra(termino, letra_a_jugar):
      for elemento in self.__elementos__:
        if elemento == termino:
          return True
    return False
  
  def realizar_pregunta(self, nombre_jugador, letra_a_jugar):
    print("%s, Porfavor escribe un/una %s que inicie con la letra %s !" % (nombre_jugador, self.get_nombre_categoria(), letra_a_jugar))
    respuesta = getpass.getpass('Respuesta: ')
    return respuesta
