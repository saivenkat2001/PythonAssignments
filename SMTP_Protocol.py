import smtplib
# smtplib is a library, which handles sending emails and routing emails

from email.message import EmailMessage
# creates a container for email message
print("server has started")
sender_email = "saivenkat.k01@gmail.com"
receiver_email = "saivenkat.k01@gmail.com"
subject = "Hello World!"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email
message.set_content("Hello, I am Sai Venkat. Nice to meet you")

server = smtplib.SMTP('smtp.gmail.com', 587)
# SMTP server object named server and connects it to the Gmail SMTP server at 'smtp.gmail.com'
# on port 587.
server.starttls()
# It is used to enable encryption (TLS or SSL) on a connection to a mail server

server.login(sender_email, "pghs wgzh hwau tyga")
# login name and password details are added

files = ['Sample.pdf','sample.jpg']
for file in files:
    with open(file,'rb') as m:
        data = m.read()

    message.add_attachment(data, maintype='image',subtype='octet-stream',filename=m.name)
    # A function used to attach the data to the email container

server.send_message(from_addr=sender_email,to_addrs=receiver_email, msg=message)

server.quit()
# closed the server
print("server has ended")

#dont hard code and use .env