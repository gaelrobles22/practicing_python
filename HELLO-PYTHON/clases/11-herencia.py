"""Para la herencia se coloca el nombre de la clase entre parentesis de la clase que se desee heredar sus metodos"""


class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Cerdito(Perro):
    def programar(self):
        print("programando")


perro = Perro()
perro.comer()
