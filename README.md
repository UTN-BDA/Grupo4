# RecorridoApp

## Autores
- Rocio Caro Caceres
- Pablo La Torre
- Lucia Garcia

## Tecnologías utilizadas

- Python
- Flask
- PostgreSQL
- Docker

## Descripción

 Es una aplicación web diseñada para gestionar y consultar los recorridos de colectivos locales y de larga distancia en **San Rafael, Mendoza**.
Permite a los usuarios acceder a información sobre rutas, horarios y paradas de transporte público, priorizando la eficiencia y escalabilidad en la gestión de datos.

Construida con **Flask** y **PostgreSQL** (gestionado con **SQLAlchemy** y **Flask-Migrate**), la aplicación se ejecuta localmente utilizando contenedores **Docker** para PostgreSQL y pgAdmin.

Implementa tres entornos aislados:
- Desarrollo
- Pruebas
- Producción

Cada uno con su propia base de datos:
- `recorrido_db`
- `test_db`
- `prod_db`

Actualmente incluye **tests unitarios** para verificar la creación de la aplicación y la conexión a la base de datos, con planes para implementar funcionalidades de consulta y gestión de recorridos.

---

## Requisitos previos

- Python 3.10 o superior (recomendado: 3.11)
- Docker y Docker Compose (para PostgreSQL y pgAdmin)
- Git (opcional, para clonar el repositorio)
- Sistema operativo compatible (probado en Windows 10/11)

---

## Instalación y configuración

### 1. Clonar el repositorio

git clone <URL_DEL_REPOSITORIO>
cd RecorridoApp

### 2. Crear y activar un entorno virtual

python -m venv venv
.\venv\Scripts\activate

### 3. Instalar dependencias

pip install -r requirements.txt

### 4. Configurar el archivo .env en RecorridoApp/

SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_RECORD_QUERIES=True

DEV_DATABASE_URI=postgresql+psycopg2://recorrido:river@localhost:5433/recorrido_db
TEST_DATABASE_URI=postgresql+psycopg2://recorrido:river@localhost:5433/test_db
PROD_DATABASE_URI=postgresql+psycopg2://recorrido:river@localhost:5433/prod_db

FLASK_CONTEXT=development

### 5. Configurar Docker en docker-postgresql/

#### Navega a docker-postgresql:

cd docker-postgresql

#### Crea un archivo .env con:

POSTGRES_USER=recorrido
POSTGRES_PASSWORD=river
POSTGRES_DB=recorrido_db

PGADMIN_DEFAULT_EMAIL=recorrido@admin.com
PGADMIN_DEFAULT_PASSWORD=river

#### Inicia los contenedores:

docker-compose up -d

### 6. Crear las bases de datos

#### Abre http://localhost:8080 y accede a pgAdmin con:

Email: recorrido@admin.com
Password: river


#### Crea un servidor:

Name: Recorrido PostgreSQL
Host: recorrido-postgresql
Port: 5432
Maintenance database: postgres
Username: recorrido
Password: river


#### En "Databases", crea:

test_db
prod_db


#### Verifica que existan recorrido_db, test_db, y prod_db.

# USO
## Ejecutar la aplicación. Asegúrate de que el entorno virtual esté activado:

.\venv\Scripts\activate


## Inicia la aplicación

flask run
Accede en http://localhost:5000 (las rutas están en desarrollo).

## Ejecutar los tests
Configura el entorno de pruebas:
bash$env:FLASK_CONTEXT="testing"

## Ejecuta los tests:
python -m unittest discover -s tests

## Los tests verifican:

Creación de la aplicación (test_app)
Conexión a test_db (test_db_connection)

