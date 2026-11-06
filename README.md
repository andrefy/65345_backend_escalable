# Aplicación Backend Escalable

## Desarrollo de un Backend Modular para una Tienda Online con FastAPI

### Objetivo

Desarrollar el backend de una tienda online utilizando FastAPI y SQLModel, implementando una arquitectura modular que permita separar responsabilidades, gestionar usuarios, autenticar solicitudes y administrar productos mediante operaciones CRUD.

### Descripción del proyecto

Se deberá desarrollar el backend de una tienda online que permita registrar usuarios, iniciar sesión y administrar un catálogo de productos.

La aplicación deberá contar con autenticación para proteger las operaciones de administración de productos y utilizar una base de datos para almacenar la información.

### 1. Estructura del proyecto

Crear el proyecto utilizando la siguiente estructura:

```
tienda/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
│
├── controller/
│   ├── auth_controller.py
│   └── producto_controller.py
│
├── core/
│   ├── config.py
│   └── security.py
│
├── db/
│   └── database.py
│
├── dependencies/
│   └── auth.py
│
├── models/
│   ├── usuario.py
│   └── producto.py
│
├── schemas/
│   ├── usuario.py
│   └── producto.py
│
└── services/
    ├── auth_service.py
    └── producto_service.py
```

Cada directorio tendrá una responsabilidad específica:

- **controller:** gestionar los endpoints y las solicitudes HTTP.
- **core:** centralizar la configuración de la aplicación y las funciones de seguridad.
- **db:** configurar la conexión y las sesiones de base de datos.
- **dependencies:** implementar dependencias reutilizables, como la validación del usuario autenticado.
- **models:** definir las tablas y entidades de la base de datos mediante SQLModel.
- **schemas:** definir los modelos de entrada y salida de la API.
- **services:** implementar la lógica de negocio y las operaciones sobre los datos.

### 2. Configuración del proyecto

- Crear un entorno virtual de Python.
- Instalar las dependencias necesarias.
- Configurar `requirements.txt` con las librerías utilizadas.
- Crear un archivo `.env` para almacenar las variables de configuración.
- Configurar `.gitignore` para excluir el entorno virtual, archivos temporales y credenciales.

Utilizar FastAPI, Uvicorn, SQLModel, un driver de base de datos y las librerías necesarias para implementar autenticación mediante JWT.

### 3. Diseño de la base de datos

La tienda deberá manejar como mínimo las siguientes entidades:

**Usuario**

- id
- username
- email
- password

**Producto**

- id
- nombre
- descripcion
- precio
- stock

Implementar los modelos correspondientes utilizando SQLModel.

Las contraseñas de los usuarios deberán almacenarse mediante un mecanismo de hash seguro, nunca como texto plano.

### 4. Implementación de autenticación

Desarrollar los siguientes endpoints:

| Método | Endpoint         | Descripción                                   |
| ------ | ---------------- | --------------------------------------------- |
| POST   | `/auth/register` | Registrar un usuario.                         |
| POST   | `/auth/login`    | Autenticar un usuario y generar un token JWT. |

Implementar las funciones necesarias para verificar las credenciales y generar el token de acceso.

### 5. Implementación del módulo de productos

Desarrollar las operaciones CRUD para administrar el catálogo de productos.

| Método | Endpoint          | Descripción                       |
| ------ | ----------------- | --------------------------------- |
| POST   | `/productos/`     | Registrar un producto.            |
| GET    | `/productos/`     | Consultar todos los productos.    |
| GET    | `/productos/{id}` | Consultar un producto específico. |
| PUT    | `/productos/{id}` | Actualizar un producto.           |
| DELETE | `/productos/{id}` | Eliminar un producto.             |

**Importante:** todas las operaciones del módulo de productos deberán estar protegidas mediante autenticación JWT. Únicamente los usuarios autenticados podrán administrar el catálogo.

### 6. Separación de responsabilidades

El desarrollo deberá respetar la arquitectura definida:

- Los controllers reciben las solicitudes y devuelven las respuestas HTTP.
- Los services contienen la lógica de negocio y las operaciones de acceso a datos.
- Los models representan las tablas de la base de datos.
- Los schemas validan los datos de entrada y estructuran las respuestas.
- Las dependencies permiten reutilizar la validación de autenticación.
- El core centraliza la configuración y las funciones de seguridad.
- El módulo db administra las sesiones y la conexión a la base de datos.

No se deberá concentrar toda la lógica de la aplicación en `main.py`.

### 7. Pruebas de funcionamiento

Utilizar la documentación automática de FastAPI (/docs) para demostrar:

1. Registro de un usuario.
2. Inicio de sesión y generación del token JWT.
3. Acceso a los endpoints de productos utilizando el token.
4. Rechazo de solicitudes sin autenticación.
5. Creación de productos.
6. Consulta de productos.
7. Actualización de productos.
8. Eliminación de productos.

## Variables de entorno

| Variable | Descripción |
| --- | --- |
| `DATABASE_URL` | URL de conexión a la base de datos (ej. `sqlite:///./database.db`) |
| `SECRET_KEY` | Clave secreta para firmar y verificar los tokens JWT |
| `ALGORITHM` | Algoritmo de cifrado del token JWT (ej. `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tiempo de expiración del token en minutos |

## Instalación

Configurar python3

```bash
python3 -m venv .venv
```

Inicializar virtual environment

```bash
source .venv/bin/activate
```

Instalar dependencias

```bash
python3 -m pip install -r requirements.txt
```

Inicializar fastapi HTTP server

```bash
fastapi dev
```

## 
