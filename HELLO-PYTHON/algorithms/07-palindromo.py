

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Ejemplo:
print(es_palindromo("Anita lava la tina"))  # Salida: True
