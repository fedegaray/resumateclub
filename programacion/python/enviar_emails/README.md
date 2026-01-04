# Enviar Emails Automáticos desde una Lista

Envía emails personalizados a una lista de contactos automáticamente.

## ¿Qué hace?

Lee un archivo CSV con nombres y correos, y envía un email personalizado a cada uno.

## Configuración inicial (solo una vez)

### Si usas Gmail:

1. Activa la verificación en dos pasos en tu cuenta de Google
2. Ve a https://myaccount.google.com/apppasswords
3. Crea una "Contraseña de aplicación" para "Correo"
4. Usa esa contraseña (no tu contraseña normal) en el script

### Configurar el script:

Abre `enviar_emails.py` y modifica:

| Variable | Qué poner |
|----------|-----------|
| `tu_email` | Tu dirección de correo |
| `tu_password` | La contraseña de aplicación (no tu contraseña normal) |
| `asunto` | El asunto del email |
| `crear_mensaje` | El cuerpo del email (puedes usar `{nombre}` para personalizar) |

## Preparar tu lista de contactos

Crea un archivo CSV con dos columnas: `nombre` y `email`

Puedes usar `contactos_ejemplo.csv` como plantilla.

## Cómo usarlo

1. Configura el script con tus datos
2. Prepara tu archivo de contactos
3. Ejecuta: `python enviar_emails.py`

## Advertencias

- Prueba primero con tu propio email para verificar que funciona
- Gmail tiene límites de envío (500 emails/día para cuentas normales)
- No uses esto para spam. En serio.

---

**Recurso de [ResuMate Club](https://www.resumateclub.com)**
