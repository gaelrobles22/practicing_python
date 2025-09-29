"""Se coloca @classmethod para indicarle que esa clase se debe ejecutar desde la clase Usuario y no desde una instancia de la clase"""


class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
