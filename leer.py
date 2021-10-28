# Packages
import poplib
from email.parser import Parser
import re

from decouple import config

# We read .env variables

user = config('user')
password = config('password')

# Connect to server
m = poplib.POP3_SSL('pop.gmail.com', 995)
m.user(user)
m.pass_(password)

# Check and read mailbox
num = len(m.list()[1])

objectives = []
for i in range(num):
    # Se lee el mensaje
    response, headerLines, bts = m.retr(i + 1)
    # Se junta el mensaje
    mensaje = '\n'.join(headerLines)
    if "No deseo que me envien más correos." not in mensaje:
        pass
    p = Parser()
    email = p.parsestr(mensaje)

    objectives.append(email["From"])

with open('clientes.txt', 'r+') as file:
    clients = file.read()
    for obj in objectives:
        clients = re.sub('', obj, clients)
        file.seek(0)
        file.write(clients)
        file.truncate
