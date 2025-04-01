import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="nombre_de_tu_base_de_datos"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM tu_tabla")

for fila in cursor.fetchall():
    print(fila)

conexion.close()
