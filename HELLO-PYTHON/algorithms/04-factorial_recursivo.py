

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo:
print(factorial(5))  # Salida: 120
