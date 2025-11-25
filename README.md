# Figures That Teach / Figuras que enseñan (Django)

Este proyecto es una aplicación web en **Django** pensada para niños, para aprender a contar usando los dedos.  
La interfaz muestra círculos/figuras que se encienden o apagan según el número de dedos detectados por un programa de visión por computadora (que se integrará aparte).

## Requisitos

- Python 3.x
- pip

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Estructura básica

- `dig_project/` – configuración principal de Django.
- `game/` – app donde vive la interfaz del juego.
- `templates/` – templates HTML (Django templates).
- `static/` – archivos estáticos (CSS, JS, imágenes).

## Ejecutar el servidor

```bash
python manage.py migrate
python manage.py runserver
```

Luego abre en el navegador: `http://127.0.0.1:8000/`


