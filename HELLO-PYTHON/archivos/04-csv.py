import csv
import os

# escribir un csv, si no lo encuentra lo crea
# se utiliza newline para indicarle que no haga salto de linea por que windows hace salto de linea al crear el archivo
# with open("archivos/archivo.csv", "w", newline='') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "este es un twit"])
#     writer.writerow([1001, 2, "otro twit"])


# leer
# with open("archivos/archivo.csv", "r") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)


# actualizar CSV
# aqui se crea un archivo temporal para modificarlo y reemplazarlo por el viejo, por eso se vuelve a renombrar
# with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w", newline='') as w:
#     reader = csv.reader(r)
#     writer = csv.writer(w)
#     for linea in reader:
#         if linea[0] == "1000":
#             writer.writerow([1000, 1, "texto modificado3"])
#         else:
#             writer.writerow(linea)

# os.remove("archivos/archivo.csv")
# os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
