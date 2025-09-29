""" Las clases abstractas se hacen para no poder crear instancias de la clase principal """

from abc import ABC, abstractmethod


class MyInterface(ABC):

    @abstractmethod
    def metodo1(self):
        pass

    @abstractmethod
    def metodo2(self):
        pass


class ClaseA(MyInterface):

    def metodo1(self):
        print("Metodo 1 - Clase A")

    def metodo2(self):
        print("Metodo 2 - Clase A")


class ClaseB(MyInterface):

    def metodo1(self):
        print("Metodo 1 - Clase B")

    def metodo2(self):
        print("Metodo 2 - Clase B")


clasea = ClaseA()
claseb = ClaseB()
