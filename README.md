Analizador de Productos mediante API

Proyecto desarrollado en Python para consumir información de productos 
mediante una API REST pùblica y almacenarla en una base de datos MySQL.

Tecnologías

- Python
- MySQL
- SQL
- API REST
- Git/GitHub

Funcionamiento

El proyecto realiza las siguientes actividades:

1. Consume información de productos desde una API REST.
2. Procesa los datos utilizando Python.
3. Conecta Python con MySQL.
4. Almacena los productos en una base de datos.
5. Permite consultar la información mediante SQL.

API utilizada

DummyJSON

La base de datos utilizada es MySQL.

Tabla principal:

- productos
  - id
  - nombre
  - precio
  - categoria
  - rating

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar:

python main.py