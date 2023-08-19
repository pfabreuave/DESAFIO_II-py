

# Este programa ainda não funciona bem, ele envia o e-mail para o primeiro 
# da lista, porém apresento-o confiando que alguém me ajudará a encontrar o erro


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Configuración de la cuenta de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'pfabreuave@gmail.com'
sender_password = 'seña de aplicacion'

# Lista de destinatarios
recipient_emails = ['pfabreuave@gmail.com', 'Lunaretornado2@gmail.com', 'sava7@hotmail.com', 'pfabreuave@hotmail.com']

# Crear el objeto MIME para el correo electrónico
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = 'Correio em massa'
body = 'Este es un correo que llegara a todos los usuarios de la lista.'
msg.attach(MIMEText(body, 'plain'))

# Iniciar la conexión al servidor SMTP de Gmail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    for recipient in recipient_emails:
        msg['To'] = recipient  # asi quedara visible para todos la lista
        #msg['Bcc'] = ', '.join(recipient_emails) # asi la lista no quedara visible
        # Enviar el correo electrónico
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f'Correo electrónico enviado a {recipient}')

except Exception as e:
    print('Error al enviar el correo electrónico:', str(e))

finally:
    # Cerrar la conexión al servidor SMTP
    server.quit()
