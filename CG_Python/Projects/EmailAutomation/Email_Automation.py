"""
Email Automation using python --> first we need to turn on 2-step verification and create app password

smtplib --> simple mail transfer protocol used for sending emails
email.mime.multipart --> used for creating emails
email.mime.text --> used for creating plain text

MIME --> multipurpose internet mail extensions
"""

import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
# import random

#Generate otp
# otp = random.randint(100000, 999999)

#first connect to gmail server
server = smtplib.SMTP("smtp.gmail.com", 587)

#now we need to start TLS encryption to make connection secure
server.starttls()

#login
server.login("vegijaykumar@gmail.com","tzsq bwxi ym3zk oaxo")

#now create the message
# msg = "This is a test email sent from Python!"
# mes = "mayaho"
msg = MIMEMultipart()

#add details
From = "vegijaykumar@gmail.com"
To = "sanjusanjay35945@gmail.com"
Subject = "read this mail"
body = "Attachment test for email automation using python"
Attachment_location = "C:/Users/vegij/OneDrive/Pictures/Saved Pictures/skin ideas/10.jpg"

msg["From"] = From
msg["To"] = To
msg["Subject"] = Subject
msg.attach(MIMEText(body))

#file attachment
part = MIMEBase('application','octet-stream')
part.set_payload(open(Attachment_location,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment', filename=os.path.basename(Attachment_location))
msg.attach(part)
text = msg.as_string()

#send the email
# server.sendmail("vegijaykumar@gmail.com","praveen545792@gmail.com", msg)
# server.sendmail("vegijaykumar@gmail.com","sanjusanjay35945@gmail.com", mes)
server.sendmail(From,To,text)

#logout
server.quit()
print("Mail sent...")

#OTP Verification
# input_ = int(input("Enter your OTP: "))
# if input_ == otp:
#     print("OTP verified...")
# else:
#     print("OTP verification failed...")

#Generate otp using math and random modules
#import math, random

#digits = "1234567890"
#otp = ""
#for i in range(6):
    #otp += digits[random.random()*10]
