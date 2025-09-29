from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = Path("modulos-nativos/plantilla.html").read_text("utf-8")
template = Template(plantilla)
cuerpo = template.substitute(usuario="Chanchito feliz")


path = Path("modulos-nativos/holamundo.jpeg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola mundo"
mensaje["to"] = "gaelrobles22@gmail.com"
mensaje["subject"] = "Esta es unaprueba"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("gael.gonzalez@cbqasolutions.com", "Robles22*")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
