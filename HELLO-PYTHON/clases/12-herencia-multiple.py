"""La herencia multiple se hace al escribir los nombre de las clases que se desea herder pero no se recomiendan mas de 3 clases
heredadas"""


class Animal:
    def comer(self):
        print("comiendo")


class Perro:
    def pasear(self):
        print("paseando")


class Cerdito(Perro, Animal):
    def programar(self):
        print("programando")


cerdito = Cerdito()
cerdito.comer()
