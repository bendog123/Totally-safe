import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
sender = 'benmc303@gmail.com'
rec = 'hotdogben3@gmail.com'
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = rec
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(sender, 'Hotdogben3')

mailserver.sendmail(sender,rec ,msg.as_string())

mailserver.quit()