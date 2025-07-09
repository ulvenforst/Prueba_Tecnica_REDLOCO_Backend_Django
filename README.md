# Rick and Morty Character Manager – Backend

Este proyecto fue desarrollado como parte de la prueba técnica para Redloco. Consiste en un backend robusto basado en **Django + PostgreSQL**, que consume la API pública de Rick and Morty y permite seleccionar, almacenar, listar y gestionar personajes desde diferentes interfaces (HTML, API REST y Django Admin).

---

## Objetivo

- Consumir personajes desde la API pública de Rick and Morty.
- Permitir seleccionar personajes desde una interfaz visual.
- Almacenar **solo los seleccionados** en PostgreSQL.
- Exponer los personajes guardados a través de una API REST interna.
- Gestionar los personajes mediante formularios HTML y desde el Django Admin.
- Soportar fallas técnicas de forma controlada.
- Contener toda la infraestructura necesaria en contenedores Docker.

---

## Tecnologías utilizadas

- **Backend**: Django 5, Django REST Framework
- **Base de datos**: PostgreSQL 15 (Docker)
- **Orquestación**: Docker + Docker Compose
- **Lenguaje**: Python 3.11+
- **API externa**: [Rick and Morty API](https://rickandmortyapi.com/api/character)

---

## Estructura del proyecto

```bash
RickAndMortyClient/
├── backend/
│   ├── characters/        # App principal (modelos, vistas, forms, API, templates)
│   ├── core/              # Configuración global de Django
│   ├── manage.py
│   ├── Dockerfile
│   └── requirements.txt
├ .env
├ .env.example
├ docker-compose.yml
└ README.md
```

---

## Instrucciones para levantar el entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/redloco-backend.git
cd redloco-backend/RickAndMortyClient
```

### 2. Crear el archivo `.env`

```bash
cp .env.example .env
```

### 3. Levantar los contenedores

```bash
docker-compose up --build
```

Esto:

- Construye el contenedor del backend.
- Levanta PostgreSQL.
- Ejecuta migraciones automáticamente.
- Expone el servidor en `http://localhost:8000`.

### 4. Crear superusuario (si es necesario)

```bash
docker compose exec backend python manage.py createsuperuser
```

Usa las credenciales deseadas o las del `.env.example`:

```
Username: root
Password: hallowaipoint1
Email: root@example.com
```

---

## Endpoints disponibles

### API REST de Personajes

| Método | Ruta                     | Descripción                             |
|--------|--------------------------|-----------------------------------------|
| GET    | `/api/characters/`       | Listar personajes guardados (DB local)  |
| POST   | `/api/characters/`       | Crear personaje manualmente (opcional)  |
| GET    | `/api/characters/{id}/`  | Ver personaje guardado                  |
| PUT    | `/api/characters/{id}/`  | Editar personaje                        |
| DELETE | `/api/characters/{id}/`  | Eliminar personaje                      |
| GET    | `/api/characters/fetch/` | Obtener personajes desde la API pública |
| POST   | `/api/characters/save/`  | Guardar personajes seleccionados por ID |

### Interfaz HTML

| Ruta                       | Funcionalidad                                   |
|----------------------------|-------------------------------------------------|
| `/select/`                 | Seleccionar personajes desde Rick and Morty API |
| `/characters/`             | Listar personajes guardados                     |
| `/characters/create/`      | Crear personaje manualmente                     |
| `/characters/edit/{id}/`   | Editar personaje                                |
| `/characters/delete/{id}/` | Eliminar personaje                              |

---

## Django Admin

```bash
Usuario: root
Contraseña: hallowaipoint1
```

Accede a: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Simulación de fallas técnicas

### Falla: Base de datos desconectada

```bash
docker compose stop db
```

Solución:

```bash
docker compose restart db
```

---

### Falla: API pública rota

Editar la URL en `characters/services/rick_and_morty_api.py`.

Solución:

- Restaurar la URL original.
- Reiniciar contenedor:

```bash
docker compose restart backend
```

---

### Falla: Error de dependencia (`requests`)

```bash
docker compose exec backend pip uninstall requests
```

Solución:

```bash
docker compose exec backend pip install requests
docker compose up --build
```

---

### Falla: Caída del backend

```bash
docker compose stop backend
```

Solución:

```bash
docker compose restart backend
```
