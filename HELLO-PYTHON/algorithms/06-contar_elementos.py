

def contar_elementos(lista):
    conteo = {}
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    return conteo

# Ejemplo:
palabras = ["manzana", "pera", "manzana", "uva"]
print(contar_elementos(palabras))
# Salida: {'manzana': 2, 'pera': 1, 'uva': 1}
