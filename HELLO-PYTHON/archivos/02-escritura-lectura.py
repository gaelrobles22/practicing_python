"""Esta es la mejor manera de trabajar con archivos """

from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")

# esto es para escribir en el archivo un hola mundo 
texto.insert(0, "Hola mundo")

#es importante usar el join para escribir sobre el archivo , si no se usa se borra todo y solo se escribe lo nuevo
archivo.write_text("\n".join(texto), "utf-8")
print(texto)
