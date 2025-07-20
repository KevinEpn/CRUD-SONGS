# CRUD Songs API

Una API REST simple construida con FastAPI y MongoDB para gestionar una colección de canciones.

## Descripción

Esta aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos de canciones. Cada canción tiene un nombre, una ruta de archivo y un contador de reproducciones.

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
├── main.py          # Punto de entrada de la aplicación FastAPI
├── models.py        # Modelos de datos con Pydantic
├── crud.py          # Operaciones CRUD
├── database.py      # Configuración de la base de datos
├── requirements.txt # Dependencias del proyecto
├── .env            # Variables de entorno (no incluir en git)
└── .gitignore      # Archivos ignorados por git
```

## Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd CRUD-Songs
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
```

3. Activa el entorno virtual:
```bash
# En Windows
.venv\Scripts\activate

# En macOS/Linux
source .venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

5. Configura las variables de entorno:
```bash
# Crea un archivo .env y añade tu URI de MongoDB
MOONGO_URI=mongodb+srv://usuario:contraseña@cluster.mongodb.net/CRUDSongs?retryWrites=true&w=majority
```

## Uso

1. Inicia el servidor:
```bash
uvicorn main:app --reload
```

2. La API estará disponible en: `http://localhost:8000`

3. Documentación interactiva: `http://localhost:8000/docs`

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
