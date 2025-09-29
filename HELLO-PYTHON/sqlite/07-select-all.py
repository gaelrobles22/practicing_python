import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    # fetchone trae todos los registros de la base de datos
    print(cursor.fetchall())
