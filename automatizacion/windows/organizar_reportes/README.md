# Organizar Reportes con Fecha

Automatiza la tarea de mover archivos y agregarles la fecha al nombre.

## ¿Qué hace?

Toma todos los archivos `.xlsx` de una carpeta origen, les agrega la fecha actual al nombre, y los mueve a una carpeta de destino.

**Ejemplo:**
- Antes: `reporte.xlsx` (en carpeta Origen)
- Después: `reporte_2026-01-04.xlsx` (en carpeta Archivo)

## Configuración

Abre `organizar_reportes.bat` con el Bloc de notas y modifica estas dos rutas:

| Qué cambiar | Valor actual | Tu valor |
|-------------|--------------|----------|
| Carpeta origen | `C:\Reportes\Origen\` | La carpeta donde están tus archivos |
| Carpeta destino | `C:\Reportes\Archivo\` | La carpeta donde quieres moverlos |

Si necesitas otro tipo de archivo (no Excel), cambia `*.xlsx` por la extensión que necesites (ej: `*.pdf`, `*.csv`).

## Cómo usarlo

### Opción 1: Ejecutar manualmente
Haz doble clic en `organizar_reportes.bat` cada vez que quieras organizar tus archivos.

### Opción 2: Programar para que se ejecute solo (recomendado)

1. Abre el menú Inicio y busca "Programador de tareas"
2. Haz clic en "Crear tarea básica"
3. Ponle un nombre (ej: "Organizar reportes lunes")
4. Elige la frecuencia (semanal) y el día (lunes)
5. Elige la hora (ej: 7:00 AM)
6. En "Acción" selecciona "Iniciar un programa"
7. Busca y selecciona tu archivo `organizar_reportes.bat`
8. Finalizar

Listo. Cada lunes a las 7:00 AM tus archivos se organizan solos.

## Nota sobre el formato de fecha

El script usa el formato de fecha de Windows en español (DD/MM/AAAA). Si tu computadora tiene otra configuración regional y la fecha aparece mal, avísanos en la comunidad y te ayudamos a ajustarlo.

---

**Recurso de [ResuMate Club](https://www.resumateclub.com)**
