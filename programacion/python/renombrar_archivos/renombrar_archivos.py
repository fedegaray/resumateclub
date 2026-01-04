import os
from datetime import datetime

carpeta = r"C:\MisArchivos"
prefijo = "VENTAS"
fecha = datetime.now().strftime("%Y-%m-%d")

for archivo in os.listdir(carpeta):
    if not archivo.startswith("."):
        nombre_nuevo = f"{fecha}_{prefijo}_{archivo}"
        os.rename(
            os.path.join(carpeta, archivo),
            os.path.join(carpeta, nombre_nuevo)
        )

print("¡Listo! Archivos renombrados.")
