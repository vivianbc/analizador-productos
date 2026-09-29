import requests
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Conexión a MySQL
conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexion.cursor()

# Obtener productos de la API
url = "https://dummyjson.com/products"
respuesta = requests.get(url)

if respuesta.status_code == 200:

    datos = respuesta.json()
    productos = datos["products"]

    for producto in productos:

        sql = """
        INSERT IGNORE INTO productos (id, nombre, precio, categoria, rating)
VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            producto["id"],
            producto["title"],
            producto["price"],
            producto["category"],
            producto["rating"]
        )

        cursor.execute(sql, valores)

    conexion.commit()

    print("Productos guardados correctamente en MySQL.")

else:
    print("Error al consultar la API.")

cursor.close()
conexion.close()