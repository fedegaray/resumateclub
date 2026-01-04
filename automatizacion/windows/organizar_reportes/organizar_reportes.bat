@echo off
set fecha=%date:~6,4%-%date:~3,2%-%date:~0,2%
for %%f in ("C:\Reportes\Origen\*.xlsx") do (
    move "%%f" "C:\Reportes\Archivo\%%~nf_%fecha%%%~xf"
)
