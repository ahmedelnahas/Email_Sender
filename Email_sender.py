from email.message import EmailMessage
import ssl
import smtplib

#the E-Mail that U want use as a Sender
Email_sender = 'spaniolandrea35@gmail.com'
# App Password Generated by Gmail U have to create two-Factor authantication to get this password
Email_password = 'djutfwqfocgrddaq'

#the Reciever and the content of the message 
Email_receiver = input("Enter the Email Reciever Plz: ")
Subject = input("Enter Ur Subject: ")
Body = input("Enter Ur Message: ")



# create instance from EmailMessage 
Em = EmailMessage()
Em['From'] = Email_sender
Em['To']= Email_receiver
Em['Subject'] = Subject
Em.set_content(Body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(Email_sender, Email_password)
    smtp.sendmail(Email_sender,Email_receiver,Em.as_string())




