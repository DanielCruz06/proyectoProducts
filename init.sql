CREATE DATABASE product_db;
CREATE DATABASE order_db;
CREATE DATABASE user_db;

-- Crear un rol con acceso a todas las bases de datos
CREATE USER myapp_user  WITH ENCRYPTED PASSWORD 'jcruz06';
GRANT ALL PRIVILEGES ON DATABASE user_db TO myapp_user;
GRANT ALL PRIVILEGES ON DATABASE product_db TO myapp_user;
GRANT ALL PRIVILEGES ON DATABASE order_db TO myapp_user;

