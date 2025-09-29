"""Todos los metodos creados en las clases deben inicializar con self
__init__ es un constructor 
"""


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("juanito", 2)
mi_perro.habla()
