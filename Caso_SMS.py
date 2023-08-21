# algunos valores no son mostrados por razones de seguridad
# debe importar pip3 install twilio

from twilio.rest import Client

# Credenciales de Twilio (necesitarás crear una cuenta en Twilio y obtener estas credenciales)
account_sid = 'TU_ACCOUNT_SID'
auth_token = 'TU_AUTH_TOKEN'

# Crear un cliente de Twilio
client = Client(account_sid, auth_token)

# Enviar un mensaje de texto
message = client.messages.create(
    body='Hola desde Python!',
    from_='+1234567890',  # Número de Twilio proporcionado
    to='+0987654321'      # Número de teléfono al que deseas enviar el mensaje
)

print(f'Mensaje enviado, SID: {message.sid}')
