# CRUD Songs API

Una API REST simple construida con FastAPI y MongoDB para gestionar una colección de canciones.

## Descripción

Esta aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos de canciones. Cada canción tiene un nombre, una ruta de archivo y un contador de reproducciones.

Este proyecto implementa un microservicio RESTful para la gestión de canciones, utilizando FastAPI como framework principal, MongoDB Atlas como base de datos en la nube y Docker para contenerización. El microservicio ha sido desplegado usando Render.com desde Docker Hub.

## Características

- ✅ Listar todas las canciones
- ✅ Crear nuevas canciones
- ✅ Actualizar canciones existentes
- ✅ Eliminar canciones
- ✅ Base de datos MongoDB
- ✅ API REST con FastAPI
- ✅ Validación de datos con Pydantic

## Tecnologías Utilizadas

- **FastAPI** - Framework web moderno y rápido para construir APIs
- **MongoDB** - Base de datos NoSQL
- **PyMongo** - Driver oficial de MongoDB para Python
- **Pydantic** - Validación de datos y configuración
- **Python-dotenv** - Gestión de variables de entorno

## Estructura del Proyecto

```
├── main.py # Punto de entrada FastAPI
├── models.py # Esquema de datos con Pydantic
├── crud.py # Funciones CRUD
├── database.py # Conexión a MongoDB Atlas
├── requirements.txt # Dependencias
├── Dockerfile # Configuración de imagen Docker
├── .dockerignore # Archivos ignorados en build
└── README.md # Este archivo
```

## 🐳 Instalación Docker

### Construcción de la imagen

```bash
docker build -t <usuario>/crud-songs .
``` 

### Ejecución de la imagen

```bash
docker run -p 10000:10000 -e MONGO_URI="mongodb+srv://<usuario>:<clave>@<cluster>.mongodb.net/CRUDSongs?retryWrites=true&w=majority" <usuario>/crud-songs
```

## Despliegue en Render

Imagen desplegada desde: Docker Hub

Plataforma: Render.com

URL del servicio (ejemplo):

```bash
https://crud-songs.onrender.com
Documentación: https://crud-songs.onrender.com/docs
``` 

## Uso

1. Visitar servicio:

Utilizar el link generado por render (ejemplo)

2. Documentación interactiva: `/docs`

## Endpoints de la API

### GET /songs
Obtiene todas las canciones.

**Respuesta:**
```json
[
  {
    "id": "<Cadena generada por Mongo>",
    "name": "Mi Canción",
    "path": "/music/mi-cancion.mp3",
    "plays": 5
  }
]
```

### POST /songs
Crea una nueva canción.

**Cuerpo de la petición:**
```json
{
  "name": "Nueva Canción",
  "path": "/music/nueva-cancion.mp3",
  "plays": 0
}
```

### PUT /songs/{song_id}
Actualiza una canción existente.

**Cuerpo de la petición:**
```json
{
  "name": "Nombre Actualizado",
  "plays": 10
}
```

### DELETE /songs/{song_id}
Elimina una canción.

## Modelos de Datos

### Song
- `name` (str): Nombre de la canción
- `path` (str): Ruta del archivo de la canción
- `plays` (int): Número de reproducciones (por defecto: 0)

### SongUpdate
- `name` (Optional[str]): Nuevo nombre de la canción
- `path` (Optional[str]): Nueva ruta del archivo
- `plays` (Optional[int]): Nuevo número de reproducciones

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.
