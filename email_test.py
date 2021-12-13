import smtplib, ssl, email, os
port = 465  # For SSL
password = "hotdogben"
import getpass as gp
#PLEASE DONT ASK ME HOW THIS WORKS IT JUST DOES
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "benmc303@gmail.com"
receiver_email = "benhotdog3@gmail.com"
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
user = gp.getuser()
subject = user
body = "This is an email with attachment sent from Python"
message = MIMEMultipart()
message["Subject"] = gp.getuser()
message["From"] = sender_email
message["To"] = receiver_email
message.attach(MIMEText(body, "plain"))

text = user



# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
