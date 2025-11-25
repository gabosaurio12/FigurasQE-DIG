#!/usr/bin/env python
import os
import sys


def main():
    """Punto de entrada para tareas administrativas de Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dig_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Asegúrate de tenerlo instalado "
            "y de que tu entorno virtual esté activado."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


