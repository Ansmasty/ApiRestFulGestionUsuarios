# ApiRestful

Este es un proyecto de API Restful desarrollado con Django y Django REST Framework.

## Requisitos

- Python 3.11
- Django 5.1.3
- MySQL
- pip (gestor de paquetes de Python)

## Instalación
situarse en Eva4RestAPIUsuarios\ApiRestful y ejecutar el comando
pip install -r requirements.txt

### Crear la base de datos

CREATE DATABASE apirestful;


#### Variables de entorno

DB_NAME=apirestful
DB_USER=root
DB_PASSWORD=su_contraseña <!-- Reemplazar por sus propias variables de entorno de mysql -->
DB_HOST=localhost
DB_PORT=3306


##### Documentación de la API

La documentación de la API esta disponible en los siguientes endpoints

Swagger: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/

###### Utilización de la API

El primer usuario debe ser creado desde la terminal con python manage.py createsuperuser

El test hecho para el uso de esta API fue utilizada con postman en el cual en headers es requerido Key = Authorization y Bearer -token luego de la creacion de este- en http://localhost:8000/api/token/ <!-- para más información sobre la creación del token ingresar la documentación antes dada -->

###### GITHUB

La aplicación esta subida en el repositorio de github 
https://github.com/Ansmasty/ApiRestFulGestionUsuarios
