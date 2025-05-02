#Email hanlding --
#SMTP protocol is used to handle emails 
#we have different SMTPS mail services for different platforms
# SMTP :-

    # gmail : smtp.gmail.com
    # hotmail : smtp.live.com
    # outlook : outlook.office365.com	or smtp.xyz.office365.com
    # yahoo : smtp.mail.yahoo.com

# While you sending email then smtp address is required 

# email: ziakayani.official@gmail.com
# app password: kjac ygho sgsr fdrr  ################################################################

import smtplib
mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()   #TLS transport layer security
connection.login(user=mymail , password=password)
connection.sendmail( from_addr=mymail, to_addrs='ziakayani888@gmail.com', msg='Hello from zia kayani')
connection.close()
print("mail has been sent")


#with subject line 
import smtplib
mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail, password=password)

SUBECT='Mail from Zia Kayani'
TEXT= "Hello there , good bye "
mymsg = 'Subject: {}\n\n{}'.format(SUBECT,TEXT)  #we must use this format
connection.sendmail(from_addr=mymail, to_addrs='ziakayani888@gmail.com', msg =mymsg)
connection.close()
print('mail has been sent !!')



#We will use new module 
import smtplib
from email.message import EmailMessage
mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"

connection =  smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail , password=password)

msg = EmailMessage()
msg['Subject']= "Hello from Zia !!"
msg['From']=mymail
msg['To']='ziakayani888@gmail.com'

msg.set_content("this is the body of email from zia kayani ")
connection.send_message(msg)
connection.close()
print("mail has been sent  !!!!")


#send attachment file as well 
import smtplib
from email.message import EmailMessage

my_mail="ziakayani.official@gmail.com"
password="kjac ygho sgsr fdrr"
connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()       #TLS transport layer security
connection.login(user=my_mail,password=password)

msg=EmailMessage()
msg['Subject']= "This is testing 2"
msg['From']= my_mail
msg['To'] = my_mail
msg['Cc'] = "ziakayani888@gmail.com"

msg.set_content("Hi team we are testing smtp server via python")

#This is attachemnt section
with open('myfile.csv','rb') as file:
    attach=file.read()
    file_name=file.name

msg.add_attachment(attach,maintype='application',subtype='octet-stream',filename=file_name)


connection.send_message(msg)
connection.close()
print("Mail has been sent")







#We will use html format in body 
import smtplib
from email.message import EmailMessage

mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"
connection =smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail , password=password)

msg = EmailMessage()
msg['Subject']= "Hello team "
msg['From']=mymail
msg['To']='ziakayani888@gmail.com'
msg['Cc']=['ziakayani888@gmail.com', 'ziakayani.official@gmail.com']

msg.add_alternative("""
                    <html> 
                        <b>hello team </b>
                        <p> messg from zia,</p>
                    </html>
                    """,subtype='html')
connection.send_message(msg)
connection.close()
print('mail sent succes')




# NEW MIME Method to send email

# MIME --> Multipurpose Internet Mail Extensions is internet standard thant extedns the format of email messages to supports text in characters set of other the ascii 
# suchh au audio , video , images and application prgram


# MIME (Multipurpose Internet Mail Extensions) is an extension of the original Simple Mail Transport Protocol (SMTP) email protocol. It lets users exchange different kinds of data files, including audio, video, images and application programs, over email.

# MIMEMultipart --> its saying i have more than one part ans listing the parts , you can implemtn text and html version

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"
connection =smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail , password=password)

msg = MIMEMultipart()
msg['Subject']= "Hello team "
msg['From']=mymail
msg['To']='ziakayani888@gmail.com'
msg['Cc']=''.join(['ziakayani888@gmail.com', 'ziakayani.official@gmail.com'])

body=""" 
<html><p> <b> <i>Hi Team,<br> This is testing email server via python script. <b> <i></p> </html> 
"""
msg.attach(MIMEText(body , 'html'))

connection.send_message(msg)
connection.close()
print('mail sent succes')



#sending attachment file 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"
connection =smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail , password=password)

msg = MIMEMultipart()
msg['Subject']= "Hello team "
msg['From']=mymail
msg['To']='ziakayani888@gmail.com'
msg['Cc'] = ', '.join(['ziakayani.official@gmail.com', 'ziakayani888@gmail.com'])

body=""" 
<html><p> <b> <i>Hi Team,<br> This is testing email server via python script. <b> <i></p> </html> 
"""
msg.attach(MIMEText(body,'html'))

#attachment section
filename= r'E:\Web Development\python learning\zia.txt'
attachment = open(filename , 'rb')
part = MIMEBase('application' , 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=%s" %filename)
msg.attach(part)

connection.send_message(msg)
connection.close()
print("Mail has been sent")



#sending logo as well l 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

mymail = "ziakayani.official@gmail.com"
password = "kjac ygho sgsr fdrr"
connection =smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail , password=password)

msg = MIMEMultipart()
msg['Subject']= "Hello team "
msg['From']=mymail
msg['To']='ziakayani888@gmail.com'
msg['Cc'] = ', '.join(['ziakayani.official@gmail.com', 'ziakayani888@gmail.com'])

body=""" 
<html><p> <b> <i>Hi Team,<br> This is testing email server via python script.  <b> <i> <br> <img src="cid:alogo" width="100" height="50"></p> </html> 
"""
msg.attach(MIMEText(body,'html'))

#logo section
file = 'E:\Web Development\python learning\logo.jpg'
mylogo= open(file , 'rb')
msgIMAGE= MIMEImage(mylogo.read())
mylogo.close()
msgIMAGE.add_header('Content-ID', 'alogo')
msg.attach(msgIMAGE)


#attachment section
filename= r'E:\Web Development\python learning\zia.txt'
attachment = open(filename , 'rb')
part = MIMEBase('application' , 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=%s" %filename)
msg.attach(part)

connection.send_message(msg)
connection.close()
print("Mail has been sent")