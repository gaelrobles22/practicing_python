from pathlib import Path
from zipfile import ZipFile

# crear un archivo comprimido con todos los archivos de nuestro proyecto
# with ZipFile("archivos/comprimidos.zip", "w") as zip:

#     for path in Path().rglob("*.*"):
#         print(path)
#           Esta linea es para decirle que si ya se encuentra comprimido no lo comprima nuevamente y se cree un bug infinito
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)


with ZipFile("archivos/comprimidos.zip") as zip:
    # esta linea es para imprimir la lista de los archivos que estan en el archivo comprimido
    print(zip.namelist())
    # esta linea es para obtener info de un documento en especifico dentro del archivo comprimido
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    # esto es para descomprimir el archivo en la ruta especificada en extracall
    zip.extractall("archivos/descomprimidos")