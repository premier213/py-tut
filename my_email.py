import smtplib
import getpass

server = smtplib.SMTP(host="smtp.gmail.com", port=587)
server.ehlo()
server.starttls()

email = input("please enter email:")
password = getpass.getpass("please enter password email:")

server.login(email, password)

from_address = email
to_address = email
subject = input("subject:")
message = input("message:")
msg = "Subject:" + subject + "\n" + message
server.sendmail(from_address, to_address, msg)
server.quit()
