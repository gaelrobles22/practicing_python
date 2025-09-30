

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo:
numeros = [5, 1, 4, 2, 8]
print(burbuja(numeros))  # Salida: [1, 2, 4, 5, 8]
