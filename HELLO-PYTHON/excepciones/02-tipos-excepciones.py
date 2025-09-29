"""Esto cacha cualquier tipo de error y lo devuelve para poder imprimirlo e identificarlo"""

try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print(type(e))

"""Este te hace a fuerzas escribir el valor que esta pidiendo, en este caso es un entero"""

try:
    n1 = int(input("Ingresa primer numero: "))
except ValueError as e:
    print("Ingresa un valor que corresponda")
