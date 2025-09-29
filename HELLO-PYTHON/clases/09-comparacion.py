class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon


coords = Coordenadas(50, 60)
coords2 = Coordenadas(50, 60)

"""esto sera falso por que compara tmb el espacio en memoria aunque los valores sean iguales, 
esto no funcionaria si no estuviera el metodo magico __eq__"""
print(coords == coords2)

"""En este caso comparamos con el metodo magico si es not equal y se utiliza el metodo  __ne__"""
print(coords != coords2)
