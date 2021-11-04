import smtplib
import email.message
import os
# Create to server object
server = smtplib.SMTP('smtp.gmail.com:587')


#Actualizamos la base de datos
user = "pp9130247@gmail.com"
password = "morrocotudo1"
# Mail content
email_content = ''
with open('mensaje.html', 'r') as file:
    for linea in file:
        email_content += linea
msg = email.message.Message()

# Mail parameters
msg['Subject'] = 'Vistaflor Newsletter'
msg['From'] = user
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

# Connect to google
server.starttls()
server.login(msg['From'], "morrocotudo1")

server.sendmail(msg['From'], "davidcruzsanchez111@gmail.com", msg.as_string())
server.close()
