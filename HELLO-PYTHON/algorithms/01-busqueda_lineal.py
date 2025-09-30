

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Devuelve la posición
    return -1  # Si no lo encuentra

# Ejemplo:
numeros = [10, 20, 30, 40]
print(busqueda_lineal(numeros, 30))  # Salida: 2
