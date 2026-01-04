import smtplib
import csv
from email.mime.text import MIMEText

# Configuración de tu correo
servidor = "smtp.gmail.com"
puerto = 587
tu_email = "tu_correo@gmail.com"
tu_password = "tu_contraseña_de_aplicacion"

# Archivo con los contactos
archivo_contactos = "contactos_ejemplo.csv"

# Asunto y cuerpo del email
asunto = "Recordatorio importante"
def crear_mensaje(nombre):
    return f"""Hola {nombre},

Este es un recordatorio automático.

Saludos,
Tu nombre"""

# Enviar emails
with open(archivo_contactos, newline='', encoding='utf-8') as f:
    contactos = csv.DictReader(f)
    
    with smtplib.SMTP(servidor, puerto) as server:
        server.starttls()
        server.login(tu_email, tu_password)
        
        for contacto in contactos:
            msg = MIMEText(crear_mensaje(contacto["nombre"]))
            msg["Subject"] = asunto
            msg["From"] = tu_email
            msg["To"] = contacto["email"]
            
            server.send_message(msg)
            print(f"Enviado a {contacto['nombre']} ({contacto['email']})")

print("¡Listo! Todos los emails enviados.")
