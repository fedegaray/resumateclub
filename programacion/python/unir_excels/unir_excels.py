import pandas as pd
import os

carpeta = r"C:\ExcelsPorUnir"
archivo_salida = r"C:\ExcelsPorUnir\consolidado.xlsx"

archivos = [f for f in os.listdir(carpeta) if f.endswith(".xlsx") and f != "consolidado.xlsx"]

dfs = []
for archivo in archivos:
    ruta = os.path.join(carpeta, archivo)
    df = pd.read_excel(ruta)
    df["_archivo_origen"] = archivo
    dfs.append(df)

consolidado = pd.concat(dfs, ignore_index=True)
consolidado.to_excel(archivo_salida, index=False)

print(f"¡Listo! {len(archivos)} archivos unidos en {archivo_salida}")
