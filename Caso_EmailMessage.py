

from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'pfabreuave@gmail.com'
email_contrasena = 'contraseña de aplicacion'
email_receptor = 'Lunaretornado2@gmail.com'

asunto = 'prueba envio correo con Python'

cuerpo = """
una contraseña específica de la aplicación es requerida 
en lugar de tu contraseña principal para autenticar la conexión SMTP. 
Esto es parte de las medidas de seguridad de Gmail para proteger tu cuenta.

Para solucionar este problema, debes generar una "contraseña de aplicación" específica para tu aplicación 
en lugar de usar tu contraseña de inicio de sesión principal. Sigue estos pasos para generar una contraseña 
de aplicación:

Inicia sesión en tu cuenta de Gmail.

Accede a la página de seguridad de tu cuenta haciendo clic en tu avatar de perfil 
en la esquina superior derecha y selecciona "Cuenta de Google".

En la barra lateral izquierda, selecciona "Seguridad".

Desplázate hacia abajo hasta la sección "Contraseña de aplicación" y selecciona "Contraseña de aplicación" 
en el menú desplegable.

Selecciona "Otro (personalizado)" en el menú desplegable y nómbralo según tu preferencia (por ejemplo, "Correo Python").

Haz clic en "Generar".

Se generará una contraseña de aplicación. Esta será la contraseña que debes usar en lugar de tu contraseña principal 
al configurar el script Python.

Luego, reemplaza 'tu_contraseña' en tu script Python con la contraseña de aplicación que generaste. 
Asegúrate de guardar la contraseña de aplicación en un lugar seguro, ya que no podrás verla nuevamente en el futuro.

Con esta contraseña de aplicación, deberías poder autenticarte correctamente en el 
servidor SMTP de Gmail y enviar correos electrónicos sin problemas.

pero si no cierto te sugiero ver este video
Como configurar el acceso de app menos seguras para el envío de correos con Gmail 2023
https://www.youtube.com/watch?v=WDxHPd1aIVE

"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)



#agregando seguridad

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())


