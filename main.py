# -*- coding: utf-8 -*-
import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"

sender_email = str(input('Type your email: '))  
receiver_email = str(input('Type the email of the receiver: '))
password = str(input("Type your password and press enter: "))

subject = str(input('Subject: '))
subject = 'Subject: ' + subject
text = str(input('Type your email body: '))
message = subject + '\n' + text

veces = int(input('Type how many emails you want to send: '))

if __name__ == '__main__':
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        for x in range(veces):
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
