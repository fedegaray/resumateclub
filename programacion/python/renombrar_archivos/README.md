# Renombrar Archivos con Fecha y Prefijo

Renombra todos los archivos de una carpeta agregándoles la fecha y un prefijo personalizado.

## ¿Qué hace?

Toma todos los archivos de una carpeta y les cambia el nombre.

**Ejemplo:**
- Antes: `reporte.xlsx`
- Después: `2026-01-04_VENTAS_reporte.xlsx`

## Configuración

Abre `renombrar_archivos.py` con cualquier editor de texto y modifica estas líneas:

| Variable | Qué poner |
|----------|-----------|
| `carpeta` | La ruta de tu carpeta (ej: `r"C:\Reportes\Enero"`) |
| `prefijo` | El texto que quieres agregar (ej: `"VENTAS"`, `"RRHH"`) |

## Cómo usarlo

1. Asegúrate de tener Python instalado
2. Abre una terminal en la carpeta del script
3. Ejecuta: `python renombrar_archivos.py`

## Advertencia

Este script modifica los nombres originales. Si quieres probarlo primero, hazlo con una carpeta de prueba con archivos que no te importen.

---

**Recurso de [ResuMate Club](https://www.resumateclub.com)**
