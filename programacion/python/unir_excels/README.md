# Unir Múltiples Archivos Excel en Uno Solo

Consolida todos los archivos .xlsx de una carpeta en un único archivo.

## ¿Qué hace?

Toma todos los archivos Excel de una carpeta, los une uno debajo del otro, y genera un archivo consolidado. Además agrega una columna indicando de qué archivo vino cada fila.

**Ejemplo:**
- Carpeta con: `enero.xlsx`, `febrero.xlsx`, `marzo.xlsx`
- Resultado: `consolidado.xlsx` con todos los datos juntos

## Requisitos

Este script necesita las librerías `pandas` y `openpyxl`. Para instalarlas:
```
pip install pandas openpyxl
```

O si tienes el archivo requirements.txt:
```
pip install -r requirements.txt
```

## Configuración

Abre `unir_excels.py` y modifica:

| Variable | Qué poner |
|----------|-----------|
| `carpeta` | La ruta donde están tus archivos Excel |
| `archivo_salida` | La ruta y nombre del archivo consolidado |

## Cómo usarlo

1. Pon todos los archivos que quieres unir en una misma carpeta
2. Asegúrate de que todos tengan la misma estructura (mismas columnas)
3. Ejecuta: `python unir_excels.py`

## Nota importante

Los archivos deben tener las mismas columnas (o al menos columnas compatibles). Si un archivo tiene columnas diferentes, aparecerán con valores vacíos en las filas de otros archivos.

---

**Recurso de [ResuMate Club](https://www.resumateclub.com)**
