# Una lista es una secuencia de datos ordenados
# puede contener distintos tipos de datos
# heterogeneos
# se pueden repetir valores


[True, 2, "a", 1.5]
# y puede mutar

lista = [29, True, 3.1415, "El numero avogadro"]

# se accede con corcetes y el numero del indice

print(lista[1])

# para cambiar un elemento podemos hacer
lista[2] = "este elemento cambie"

print(lista)


########
# funciones que ofrece una lista

lista_nueva = [1, 2, 3, 4, 5]

# con este agregas un elemento al final
lista_nueva.append(3)

# con este cuentas cuantas veces se repite un elemento
print(lista_nueva.count(3))

# este devuelve la posicion de un elemento 
