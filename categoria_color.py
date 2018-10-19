import categoria

# Categoria de nombres, usa la herencia de la programacion orientada a objetos
# para hacer uso de los metodos de la clase a la que hereda
class CategoriaColor(categoria.Categoria):

  def __init__(self, elementos):
    # llama al constructor de la clase padre, en este caso,
    # seteando el nombre del la categoria y
    # seteando tambien la lista de las palabras validas para esta
    categoria.Categoria.__init__(self, "color", elementos)

  