#!/usr/bin/python
import smtplib

fromaddr = 'cmclaren89@gmail.com'
toaddr  = 'craigh89@yahoo.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
fromname = "Craig"
toname = "rascal"
subject = "test"
msg = "hello world"
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'cmclaren89@gmail.com'
password = 'uwdaqbgqxdmhbdzo'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()