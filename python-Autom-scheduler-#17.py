#we can schedulat the tasks in python 
#for linux we use  -  crontab
#for windows we use  - task scheduler
#for platform independent -   we use python scheduler

#Task will run every 10 seconds
import schedule
import time
def abd():
    print("This is testing message via schedule")

schedule.every(10).seconds.do(abd)

while True:
    schedule.run_pending()
    time.sleep(1)


#with time 
import schedule
import time
import datetime
def abd():
    now = datetime.datetime.today()
    print('the current time is ', now)

schedule.every(10).seconds.do(abd)

while True:
    schedule.run_pending()
    time.sleep(1)

#every 10 minutes
import schedule
import time
import datetime
def abd():
    now = datetime.datetime.today()
    print('the current time is ', now)

schedule.every(10).minutes().do(abd)

while True:
    schedule.run_pending()
    time.sleep(1)


#Run task at 09:03 PM 
import schedule
import time
import datetime
def abd():
    now = datetime.datetime.today()
    print('the current time is ', now)

schedule.every().day.at('21:03').do(abd)

while True:
    schedule.run_pending()
    time.sleep(1)

#################################################
job1=schedule.every().day.at("21:03").do(abd)
job2=schedule.every(10).minutes.do(abd)
job3=schedule.every(10).seconds.do(abd)
job4=schedule.every(10).hours.do(abd)

job2=schedule.every(5).minutes.do(abd)


###every 5 hours 
job4=schedule.every(5).hours.do(abd)

##Every 5 of the weeks 
job4=schedule.every(5).weeks.do(abd)

#every monday i need to run the task
job4=schedule.every().monday.do(abd)

#i want to run task at sunday exact 6:00 AM 
job4=schedule.every().sunday.at("06:00").do(abd)



##   Our project :-
import schedule
import time as t
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import datetime

def abd():
    day = datetime.today()
    time = datetime.now()

    my_custom = day.strftime("%B %d %Y")
    current_time = time.strftime("%I:%M:%S %p")

    filename = r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 40\test.txt"
    mylogo = r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 40\alnafi.jpg"
    msg = MIMEMultipart()

    my_mail = "automation52786@gmail.com"
    password = "nrjxoxmahyxzybvm"
    msg['Subject'] = f"Citrix connection alert {my_custom} {current_time}"
    msg['From'] = my_mail
    msg['To'] = my_mail
    msg['Cc'] = 'abdealipython@gmail.com'

    body = """ 
    <html><p> <b> <i>Hi Team,<br> This is testing email server via python script. 
    <b> <i> <br> <img src="cid:alogo" width="100" height="50"></p> </html> 
    """
    msg.attach(MIMEText(body, 'html'))

    ###LOGO section
    filelogo = open(mylogo, 'rb')
    msgIMAGE = MIMEImage(filelogo.read())
    filelogo.close()
    msgIMAGE.add_header('Content-ID', '<alogo>')
    msg.attach(msgIMAGE)

    # ATTACHMENT section
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    msg.attach(part)

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()  # TLS transport layer security

    connection.login(user=my_mail, password=password)
    connection.send_message(msg)
    connection.close()
    print("Mail has been sent")

schedule.every().day.at("21:15").do(abd)

while True:
    schedule.run_pending()
    t.sleep(1)








# app password =  tjid vlwi qwbn etje
