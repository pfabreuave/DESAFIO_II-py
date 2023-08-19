import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import os

# Configuración de la cuenta de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'pfabreuave@gmail.com'
sender_password = 'seña de aplicacion'

# Crear el objeto MIME para el correo electrónico
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = 'pfabreuave@gmail.com'
msg['Subject'] = 'Correo via Python pana mi'

# Agregar el cuerpo del correo
body = 'este es un mss de prueba enviado desde python'
msg.attach(MIMEText(body, 'plain'))

# Adjuntar una imagen (opcional)
image_path = 'ruta/a/la/imagen.jpg'
if os.path.exists(image_path):
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read())
        image.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
        msg.attach(image)

# Iniciar la conexión al servidor SMTP de Gmail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Enviar el correo electrónico
    server.sendmail(sender_email, msg['To'], msg.as_string())
    print('Correo electrónico enviado correctamente.')

except Exception as e:
    print('Error al enviar el correo electrónico:', str(e))

finally:
    # Cerrar la conexión al servidor SMTP
    server.quit()


# una contraseña específica de la aplicación es requerida 
# en lugar de tu contraseña principal para autenticar la conexión SMTP. 
# Esto es parte de las medidas de seguridad de Gmail para proteger tu cuenta.

# Para solucionar este problema, debes generar una "contraseña de aplicación" específica para tu aplicación 
# en lugar de usar tu contraseña de inicio de sesión principal. Sigue estos pasos para generar una contraseña 
# de aplicación:

# Inicia sesión en tu cuenta de Gmail.

# Accede a la página de seguridad de tu cuenta haciendo clic en tu avatar de perfil 
# en la esquina superior derecha y selecciona "Cuenta de Google".

# En la barra lateral izquierda, selecciona "Seguridad".

# Desplázate hacia abajo hasta la sección "Contraseña de aplicación" y selecciona "Contraseña de aplicación" 
# en el menú desplegable.

# Selecciona "Otro (personalizado)" en el menú desplegable y nómbralo según tu preferencia (por ejemplo, "Correo Python").

# Haz clic en "Generar".

# Se generará una contraseña de aplicación. Esta será la contraseña que debes usar en lugar de tu contraseña principal 
# al configurar el script Python.

# Luego, reemplaza 'tu_contraseña' en tu script Python con la contraseña de aplicación que generaste. 
# Asegúrate de guardar la contraseña de aplicación en un lugar seguro, ya que no podrás verla nuevamente en el futuro.

# Con esta contraseña de aplicación, deberías poder autenticarte correctamente en el 
# servidor SMTP de Gmail y enviar correos electrónicos sin problemas.

# pero si no cierto te sugiero ver este video
# Como configurar el acceso de app menos seguras para el envío de correos con Gmail 2023
# https://www.youtube.com/watch?v=WDxHPd1aIVE






