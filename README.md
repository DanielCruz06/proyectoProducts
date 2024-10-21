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
# Microservices API Project

Este proyecto es una API basada en microservicios que permite la gestión de usuarios, productos y órdenes. La aplicación está desarrollada utilizando **Flask** y cada microservicio se conecta a una base de datos **PostgreSQL**.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Arquitectura](#arquitectura)
- [Instalación y Configuración](#instalación-y-configuración)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Servicios Disponibles](#servicios-disponibles)
- [Pruebas con curl](#pruebas-con-curl)
- [Notas Adicionales](#notas-adicionales)

## Descripción del Proyecto

El objetivo de este proyecto es proporcionar una API simple basada en microservicios que incluya la funcionalidad de registrar usuarios, iniciar sesión, gestionar productos y generar órdenes. Los microservicios se orquestan utilizando Docker Compose y se despliegan con contenedores de Docker.

## Arquitectura

El proyecto se compone de los siguientes microservicios:

1. **User Service**: Maneja la gestión de usuarios (registro e inicio de sesión).
2. **Product Service**: Permite la creación, edición y eliminación de productos.
3. **Order Service**: Gestiona la creación de órdenes basadas en productos.
4. **Base de Datos**: Utiliza PostgreSQL como sistema de base de datos para todos los microservicios.

## Instalación y Configuración
## Instalación y Configuración

### Prerrequisitos

Antes de iniciar la instalación, asegúrate de tener instaladas las siguientes herramientas en tu sistema:

1. **Docker**: Para instalar Docker, sigue la [guía de instalación oficial](https://docs.docker.com/get-docker/) para tu sistema operativo.
2. **Docker Compose**: Instala Docker Compose siguiendo esta [guía oficial](https://docs.docker.com/compose/install/).
3. **Git**: Instala Git desde su [sitio web oficial](https://git-scm.com/) si aún no lo tienes instalado.

### Clonar el Repositorio

1. **Abre una terminal** y navega al directorio donde deseas clonar el repositorio.
2. Ejecuta el siguiente comando para clonar el repositorio desde GitHub:

   ```bash
   git clone https://github.com/DanielCruz06/proyectoProducts.git


### Prerrequisitos

- **Docker**: Asegúrate de tener Docker instalado en tu máquina. Puedes instalarlo siguiendo [esta guía](https://docs.docker.com/get-docker/).
- **Docker Compose**: Necesario para orquestar múltiples contenedores. Puedes instalarlo siguiendo [esta guía](https://docs.docker.com/compose/install/).
- **Git**: Para clonar y gestionar el repositorio.

### Instalación de Dependencias

#### Clonar el Repositorio

```bash
git clone https://github.com/DanielCruz06/proyectoProducts.git
cd proyectoProducts

