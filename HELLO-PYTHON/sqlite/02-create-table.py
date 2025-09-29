import sqlite3

con = sqlite3.connect("sqlite/app.db")
# cursor es un intermediario entre la base de datos y nosotros la cual le enviaremos consultas a traves de ese comando
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
# commit es necesario para que la consulta a la base de datos se realice SI O SI
con.commit()
con.close()
