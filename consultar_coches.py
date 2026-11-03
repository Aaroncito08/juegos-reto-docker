import json
import mysql.connector
from pathlib import Path

# Leer la configuración de MySQL
ruta = Path(__file__).with_name("config.json")

with open(ruta, "r", encoding="utf-8") as archivo:
    config = json.load(archivo)

# Conectar a MySQL
conexion = mysql.connector.connect(**config)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")

for coche in cursor.fetchall():
    print(coche)

cursor.close()
conexion.close()
