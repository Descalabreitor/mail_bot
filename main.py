# Packages
import smtplib
import email.message

# Create to server object
server = smtplib.SMTP('smtp.gmail.com:587')

# Mail content
email_content = ''
with open('mensaje.html', 'r') as file:
    for linea in file:
        email_content += linea
msg = email.message.Message()

# Mail parameters
msg['Subject'] = 'Vistaflor Newsletter'
msg['From'] = 'pp9130247@gmail.com'
password = '1qaz<xsw23edc'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

# Connect to google
server.starttls()
server.login(msg['From'], password)

# Sending mails
clients = []
with open('clientes.txt','r') as file:
    for linea in file:
        clients.append(linea[:-1])

for client in clients:
    msg['To'] = client
    server.sendmail(msg['From'], client, msg.as_string())
    msg['To'] = ''