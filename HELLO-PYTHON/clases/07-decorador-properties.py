class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        """strip se utiliza para eliminar los espacios en blanco al principio y al final de un string"""
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Chanchito")
print(perro.nombre)
