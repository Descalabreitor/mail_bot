# Packages
import os
import re
import hashlib
from imap_tools import MailBox


# We read .env variables
def update_clients(user, password):

    # Connect to server
    mailbox = MailBox(user+'gmail.com')
    mailbox.login(user, password)

    for m in mailbox.fetch():
        cuerpo = ''
        subject = m.subject
        print(subject)
    mailbox.logout()

    with open('clientes.txt', 'r+') as file:
        clients = file.read()
        for obj in objectives:
            clients = re.sub('', obj, clients)
            file.seek(0)
            file.write(clients)
            file.truncate
