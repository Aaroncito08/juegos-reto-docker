import json
import mysql.connector
from pathlib import Path
from prettytable import PrettyTable

# Leer configuración
ruta = Path(__file__).with_name("config.json")

with open(ruta, "r", encoding="utf-8") as archivo:
    config = json.load(archivo)

# Conectar a MySQL
conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

cursor.execute("SELECT * FROM coches")

# Crear tabla
tabla = PrettyTable(["ID", "Marca", "Modelo", "Color", "KM", "Precio"])

for coche in cursor.fetchall():
    tabla.add_row(coche)

print(tabla)

cursor.close()
conexion.close()
