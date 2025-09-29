"""Las anotaciones @classmethod es para especificar metodos exclusivos de la clase y se le pasa el cls"""


class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 2)


Perro.habla()
perro1 = Perro("Juanito1", 2)
perro2 = Perro("Juanito2", 2)
perro3 = Perro.factory()

print(perro3.edad, perro3.nombre)
