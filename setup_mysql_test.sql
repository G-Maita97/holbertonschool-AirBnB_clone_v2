-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Crear el usuario si no existe
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Otorgar todos los privilegios en la base de datos al usuario
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Otorgar permiso SELECT en performance_schema al usuario
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
