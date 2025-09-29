"""Para hacer un dato o metodo privado se le colocan dos guiones bajos antes de la propiedad o del metodo"""


class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 2)


perro1 = Perro.factory()
perro1.habla()

"""Esto se hace para saber las propiedades que estan privadas y las lista usando __dict__"""

print(perro1.__dict__)
