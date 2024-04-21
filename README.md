# Django Project API

Este proyecto forma parte del segundo desafío del challenge enviado, el cual implica la creación de una API REST utilizando Django para gestionar proyectos. La API utiliza JWT para la autenticación, validando los tokens con un servicio de backend externo desarrollado en el primer desafío.

## Tecnologías Utilizadas

- **Django y Django REST Framework**: Utilizados para construir la API REST.
- **Docker**: Empleados para contenerizar la aplicación y garantizar consistencia entre diferentes entornos de desarrollo y producción.
- **SQLite**: Base de datos por defecto de Django utilizada para almacenar los datos de los proyectos.
- **Python**: Lenguaje de programación en el que se basa Django.

## Estructura del Proyecto

Descripción breve de cómo está organizado el proyecto:

- `/projects`: Contiene el modelo, vistas, serializadores y rutas para la gestión de proyectos.
- `/authentication`: Maneja la autenticación de usuarios con JWT verificando con el backend del primer desafío.
- `docker-compose.yml`: Configuración para la orquestación de los contenedores Docker.

## Cómo Ejecutar Localmente

Instrucciones paso a paso para clonar y ejecutar el proyecto:

### Clonar el Repositorio

`git clone URL_DEL_REPOSITORIO`

### Ejecutar con Docker Compose

Deberías tener Docker y Docker Compose instalados en tu sistema. Luego, ejecutar:

```bash
docker-compose up --build
```

Esto levantará la API en el puerto 8000.

### Acceder a la Aplicación

API: La API estará accesible en http://localhost:8000/projects/ donde se pueden realizar operaciones CRUD sobre los proyectos.

### Funcionalidades

- CRUD de Proyectos: Crear, leer, actualizar y eliminar proyectos.
- Autenticación de Usuarios: Asegura que solo usuarios autenticados puedan realizar operaciones en la API.
- Integración con Backend Externo: Utiliza un servicio externo para validar JWTs y obtener información del usuario.
