import sqlite3

# esta manera de hacerlo es para no tener que escribir siempre commit ni close por que tiene el metodo magico __exit__
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
