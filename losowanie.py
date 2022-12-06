import random
from email.message import EmailMessage
import ssl
import smtplib
import os

people = {
    #write your group of people here
}

emaile = list(people.values())
imiona = list(people.keys())
global imie
global email


for i in range(11):
        def randomPick():
            if len(emaile)>0:
                email = random.choice(emaile)
                imie = random.choice(imiona)
                if email == people[imie]:
                    if len(emaile) == 1:
                        None
                    else:
                        randomPick()
                imie = imie
                email = email
                emaile.remove(email)
                imiona.remove(imie)
                return imie, email
            else:
                print('koniec listy')


        email_sender = "write your email here"
        flags = os.O_RDONLY
        myFile = os.open('PATH TO YOUR PASSWORD FILE', flags)
        myData = os.read(myFile, 105)
        email_password = myData.decode("UTF-8")

        email_receiver_name, email_receiver_email = randomPick()


        subject = 'Write your subject here'
        body = f""""Write you body here"""
        msg = EmailMessage()
        msg['From'] = email_sender
        msg['To'] = email_receiver_email
        msg['Subject'] = subject
        msg.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_sender, msg.as_string())

