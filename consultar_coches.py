import os
import mysql.connector

conexion = mysql.connector.connect(
    host="reto4-mysql",
    user="root",
    password=os.environ["MYSQL_PASSWORD"],
    database="coches_db"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")

for coche in cursor.fetchall():
    print(coche)

cursor.close()
conexion.close()
