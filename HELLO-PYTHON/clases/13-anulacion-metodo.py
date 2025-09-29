"""Se anota la palabra super para utilizar los metodos que se llamen igual de la clase padre"""


class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("Ave voladora")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        print("Pato volador")
        super().vuela()


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
