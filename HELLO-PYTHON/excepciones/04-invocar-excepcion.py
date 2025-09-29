"""Podemos ver todas las excepciones en la documentacion de python en https://docs.python.org/3/library/exceptions.html
Se utiliza raise en vez de return para las excepciones"""


def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)
