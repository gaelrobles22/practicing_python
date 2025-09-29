from pathlib import Path

# Path(r"C:\Archivos de programa\Minecraft")
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

# Esto sirve para cambiarle el nombre y tipo de archivo
p = path.with_name("chanchito.py")
print(p)
# Esto sirve para cambiarle el tipo de archivo
p = path.with_suffix(".bat")
print(p)
# Esto sirve para cambiarle el nombre al archivo creado
p = path.with_stem("feliz")
print(p)
