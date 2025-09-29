# son elementos no ordenados
# heterogeneos
# son mutables
# no se repiten

# a diferencia de los diccionarios los conjuntos se pone set para inicializar, si hay algun elemento repetido lo elimina
print(set([5, 2, 5, 1, 1.5]))

conjunto = set([2, 3, 3, 4])
# print(conjunto)


# podemos anadir elementos
conjunto.add(1)
# print(conjunto)

# elminar elemento
conjunto.remove(1)
# print(conjunto)

# se pueden hacer intersecciones entre conjuntos esto para ver cuales elementos tiene en comun
conjunto_2 = set([5, 3, 5, 6, 2])
conjunto_3 = set([4, 2])
print(conjunto_2.intersection(conjunto_3))
# tambien se puede representar de la siguiente manera
print(conjunto_2 & conjunto_3)

#Los siguientes operadores que se pueden usar son
conjunto_2|conjunto_3 #union
conjunto_2-conjunto_3 #diferencia
conjunto_2>=conjunto_3 #superconjunto
conjunto_2 & conjunto_3 #insterseccion
conjunto_2 ^ conjunto_3 #diferencia simetrica
conjunto_2 <= conjunto_3 #subconjunto
