# Packages
import imaplib
import email
from email.header import decode_header


def update_clients(username, password, clients):
    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)

    status, messages = imap.select("INBOX")
    # total number of emails

    messages = int(messages[0])

    subjects = []
    objectives = []

    for i in range(messages):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)
                subjects.append(subject)
                objectives.append(From)
    for subject in subjects:
        if subject == 'Desubscripción':
            del clients[objectives[subjects.index(subject)]]
        # close the connection and logout
    imap.close()
    imap.logout()
