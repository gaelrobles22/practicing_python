# """from e import pueden usuarse para importar metodos de otros archivos pero no se recomienda usar el * no es bueno es mejor
# especificar cada uno de los metodos o el paquete y el archivo"""

# # Estas son las 3 formas de importar y abajo son sus formas de traer el metodo
# import usuarios.acciones
# from usuarios.acciones import guardar
# from usuarios import acciones


# usuarios.acciones.guardar()  # import usuarios.acciones
# guardar()  # from usuarios.acciones import guardar
# acciones.guardar()  # from usuarios import acciones

# # La mas recomendables son, que son menos tediosas tambien
# # from usuarios.acciones import guardar
# # from usuarios import acciones

from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios

print(dir(usuarios))
