# Packages
import poplib
from email.parser import Parser
import re
import os


# We read .env variables
def update_clients(user, password):

    # Connect to server
    m = poplib.POP3_SSL('pop.gmail.com', 995)
    m.user(user)
    m.pass_(password)

    # Check and read mailbox
    num = len(m.list()[1])

    objectives = []
    for i in range(num):
        # Se lee el mensaje
        response, header_lines, bts = m.retr(i + 1)
        # Se junta el mensaje
        mensaje = '\n'.join(header_lines)
        print(mensaje)
        p = Parser()
        email = p.parsestr(header_lines)
        print(str(email['From']))
        objectives.append(email["From"])

    with open('clientes.txt', 'r+') as file:
        clients = file.read()
        for obj in objectives:
            clients = re.sub('', obj, clients)
            file.seek(0)
            file.write(clients)
            file.truncate
