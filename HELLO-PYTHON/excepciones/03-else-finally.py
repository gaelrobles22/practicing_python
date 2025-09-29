try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un error")
else:
    print("No ocurrio ningun error")


try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un error")
finally:
    print("se ejecuta siempre")


try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un error")
else:
    print("Ocurrio un error")
finally:
    print("se ejecuta siempre")
