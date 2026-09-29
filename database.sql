CREATE DATABASE analizador_productos;

USE analizador_productos;

CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(150),
    precio DECIMAL(10,2),
    categoria VARCHAR(100),
    rating DECIMAL(3,2)
);