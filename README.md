crear entorno virtual
*
sudo python3 -m venv venv 
source venv/bin/activate

* salirse: 
deactivate

Data bases mysql:
CREATE USER 'proyecto'@'localhost' IDENTIFIED BY 'josecruz06';

modulos para venv
pip install Flask-Login
pip install Flask-SQLAlchemy
pip install mysqlclient


# instalación de librerias 
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
