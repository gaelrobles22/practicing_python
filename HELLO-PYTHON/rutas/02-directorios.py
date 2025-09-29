from pathLib import Path

path = Path("rutas")
path.exists()
path.mkdir()  # crear
path.rmdir()  # remove directory
path.rename("chanchito-feliz")

for p in path.iterdir():
    print(p)
