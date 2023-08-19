
# Este procedimiento automatiza la creación de copias de seguridad de archivos y carpetas, 
# las organiza en una carpeta con nombre de fecha y hora, 
# las comprime en un archivo ZIP y 
# finalmente elimina la carpeta de copia de seguridad original
# se envia msj al usuario via whatsapp



import os
import shutil
import zipfile
from datetime import datetime

import pywhatkit as pwk

def enviar_mensaje_whatsapp(numero, mensaje):
    # Enviar mensaje por WhatsApp
    pwk.sendwhatmsg_instantly(numero, mensaje)


def crear_copia_de_seguridad(origen, destino):
    # Crear una carpeta con la fecha y hora actual como nombre
    fecha_hora_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
    carpeta_destino = os.path.join(destino, f"Copia_{fecha_hora_actual}")
    os.makedirs(carpeta_destino)

    # Copiar archivos y carpetas al destino
    for elemento in os.listdir(origen):
        origen_absoluto = os.path.join(origen, elemento)
        if os.path.isfile(origen_absoluto):
            shutil.copy(origen_absoluto, carpeta_destino)
        elif os.path.isdir(origen_absoluto):
            shutil.copytree(origen_absoluto, os.path.join(carpeta_destino, elemento))

    # Comprimir la carpeta de copia de seguridad en un archivo ZIP
    nombre_archivo_zip = os.path.join(destino, f"Copia_{fecha_hora_actual}.zip")
    with zipfile.ZipFile(nombre_archivo_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for raiz, _, archivos in os.walk(carpeta_destino):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                ruta_relativa = os.path.relpath(ruta_completa, carpeta_destino)
                zipf.write(ruta_completa, ruta_relativa)

    # Eliminar la carpeta de copia de seguridad no comprimida
    
    shutil.rmtree(carpeta_destino)

# Rutas de origen y destino
ruta_origen = "/Users/pfabreuave/OneDrive/Área de Trabalho/origen"
ruta_destino = "/Users/pfabreuave/OneDrive/Área de Trabalho/destino"

# Crear la copia de seguridad
crear_copia_de_seguridad(ruta_origen, ruta_destino)



# Enviar mensaje por WhatsApp
numero_whatsapp = "+5511992769388"  # Reemplazar con el número de WhatsApp del destinatario
mensaje_whatsapp = "Se ha realizado una copia de seguridad exitosamente."
enviar_mensaje_whatsapp(numero_whatsapp, mensaje_whatsapp)
