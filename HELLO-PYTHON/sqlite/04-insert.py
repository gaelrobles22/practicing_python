import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    # nunca se debe pasar un string formateado a una consulta de datos siempre van despues de la consulta
    cursor.execute(
        "insert into usuarios values(?, ?)",
        # aqui se muestra que es primero la consulta y luego la info
        (1, "Hola Mundo"),
    )
