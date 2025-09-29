from io import open

# escritura
# texto = "hola mundo"

# aqui se pone la ruta del archivo y se pone la opcion que se utilizara en este caso w de write
# si el archivo no existe python lo va a crear solo
# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# #siempre se debe cerrar el archivo
# archivo.close()


# lectura

# aqui se pone la ruta del archivo y se pone la opcion que se utilizara en este caso r de read
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()

# lectura como lista
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()

# with y seek
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)  # esto es para indicarle que se regrese a la primera linea
#     for linea in archivo:
#         print(linea)

# agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("chao mundo")
# archivo.close()

#lectura y escritura

# with open("archivos/hola-mundo.txt", "r+") as archivo:
#     texto = archivo.readlines()
#     archivo.seek(0)
#     texto[0] = "Chanchito feliz"
#     archivo.writelines(texto)
