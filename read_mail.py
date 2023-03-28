import imaplib
import getpass

server = imaplib.IMAP4_SSL("imap.gmail.com")

email = "premierp1213@gmail.com"
password = "xqphyedbpeapwksu"

server.login(email, password)
print(server.list())

server.select('inbox')

type, data = server.search(None, 'FROM "noreply@medium.com"')

email_id = data[0]

print(email_id)

result, email_data = server.fetch(email_id, "(RFC822)")

print(result)
