# No tiene orden
# son estructurados por llave valor
# {key: value, key: value}
# son heterogeneos
# son mutables


diccionario = {1: "uno", 2: "Dos"}
diccionario["culon"] = "culito"
print(diccionario["culon"])

# las keys no se pueden repetir por ejemplo

dict_repeticion = {1: "Primero", 1: "Ultimo"}
print(dict_repeticion)
# en caso que se repita la key toma el ultimo valor proporcionado en este caso Ultimo

#los metodos que ofrecen los diccionarios son
print("//////////")
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

#para eliminar la clave y valor usamos pop indicando la key
diccionario.pop(2)
print(diccionario)