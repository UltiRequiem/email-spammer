# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from time import sleep
from random import randint

username =  str(input('Type your email: ')) 
password = str(input("Type your password: "))

def start_server():
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server

def send_emails(server):
    emails = "".join(open("victims.txt", "r").read().split()) 
    for email in range(100):
        #print(str(email) + ' emails have been sent.') 
        msg = MIMEText("This is a cool message.If you want revenge here is how: https://github.com/UltiRequiem/gmail-spammer")
        msg['Subject'] = 'Cool Spam ' + str(randint(1, 1000)) 
        msg['From'] = username
        msg['To'] = emails
        server.sendmail(username, emails, msg.as_string())

def main():
    while True:
        server = start_server()
        try:
            send_emails(server)
        except Exception as e:
            sleep(60) 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted program. Exitting...")
