import os
from pymongo import MongoClient
from prettytable import PrettyTable

# Conexión a MongoDB
cliente = MongoClient(
    host="reto8-mongo",
    port=27017,
    username="admin",
    password=os.environ["MONGO_PASSWORD"],
    authSource="admin"
)

# Seleccionar base de datos y colección
db = cliente["concesionario"]
coleccion = db["coches"]

# Mostrar los coches en una tabla
tabla = PrettyTable(["ID", "Marca", "Modelo", "Color", "KM", "Precio"])

for coche in coleccion.find().sort("id", 1):
    tabla.add_row([
        coche["id"],
        coche["marca"],
        coche["modelo"],
        coche["color"],
        coche["km"],
        coche["precio"]
    ])

print(tabla)
cliente.close()
