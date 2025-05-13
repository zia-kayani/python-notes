# --------- Remote server modules-------- :-

# Paramiko module will use for remote server script.

# Open source python-paramiko 
# it used by IBM netezza host management
# Paramiko is python implementation of the SSHv2 protocols , providing both client and server functionality 
# Paramiko is python library tha makes connection with remote server via ssh. 
# it will connect via two way communcation - on client and server paramiko installation is required

import paramiko
hostname = '192.168.241.204'
username = 'zia'
password ='zia123'
client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd = 'df -h'
stdin,stdout,stderr = client.exec_command(mycmd)
mycmdout =  stdout.read()
print(mycmdout)


################
import paramiko
hostname = '192.168.241.204'
username = 'zia'
password ='zia123'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd="df -h"


stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stdout.readlines()

for i in mycmdout:
    print(i)

#############################
import paramiko
hostname = '192.168.241.204'
username = 'zia'
password ='zia123'
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd="df -h"
stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stdout.readlines()

for i in mycmdout:
    print(i.strip('\n'))

######################
import paramiko
hostname = '192.168.241.204'
username = 'zia'
password ='zia123'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd="df -h"


stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stdout.read().decode()
print(mycmdout)

########################
import paramiko
hostname = '192.168.241.204'
username = 'zia'
password ='zia123'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd="dddd"  #if i apply wrong command


stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stderr.read().decode()
print(mycmdout)

###################################
import paramiko
hostname = '192.168.241.204'
username = 'zia'
password ='zia123'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd="df -h"


stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stdout.readlines()
print(mycmdout[0])
print(mycmdout[1].split()) #in order to see on specific line and specifc value





# ------- passwordless connection or authuntication ------------
# in order to access a machine without password for this we generate a private key in agent machine and then add that in 
# in master machine and then we can easyliy access the agent machine

# following are the steps :-
# 1-    ssh-keygen
# 2-    home/zia/.ssh
# 3-    ls -ltrh id_rsa
# 4-    ssh-copy-id <master-ip>

# scp username@192.168.x.x:/home/username/.ssh/id_rsa   C:\Users\Zia\ssh\myprivatekey.pem  
# mv id_rsa pricate_key   #on master

#!/usr/bin/python

import paramiko
hostname = '192.168.112.128'
username = 'zia'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file("/home/zia/.ssh/id_rsa")

client.connect(hostname=hostname,username=username, pkey=key)

mycmd="df -h"


stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stdout.read().decode()
print(mycmdout)
client.close()


#to get  > 80% storage details
#!/usr/bin/python
import paramiko
hostname = '192.168.112.128'
username = 'zia'

client =  paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("/home/zia/.ssh/id_rsa")
client.connect(hostname=hostname,username=username,pkey=key)

mycmd ="df -h"

stdin, stdout, stderr =  client.exec_command(mycmd)

mycmdout = stdout.readlines()
for i in mycmdout:
    print(i.split()[4])
client.close()


#to remove header 
#!/usr/bin/python
import paramiko
hostname = '192.168.112.128'
username = 'zia'

client =  paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("/home/zia/.ssh/id_rsa")
client.connect(hostname=hostname,username=username,pkey=key)

mycmd ="df -h"

stdin, stdout, stderr =  client.exec_command(mycmd)

mycmdout = stdout.readlines()
for i in mycmdout[1:]:
    print(i)
client.close()


#to remove percentage 
#!/usr/bin/python
import paramiko
hostname = '192.168.112.128'
username = 'zia'

client =  paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("/home/zia/.ssh/id_rsa")
client.connect(hostname=hostname,username=username,pkey=key)

mycmd ="df -h"

stdin, stdout, stderr =  client.exec_command(mycmd)

mycmdout = stdout.readlines()
for i in mycmdout[1:]:
    full_size = (i.split()[4])
    print(full_size.replace('%',' '))
client.close()

#final script
#!/usr/bin/python
import paramiko
hostname = '192.168.112.128'
username = 'zia'

client =  paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("/home/zia/.ssh/id_rsa")
client.connect(hostname=hostname,username=username,pkey=key)

mycmd ="df -h"

stdin, stdout, stderr =  client.exec_command(mycmd)

mycmdout = stdout.readlines()
for i in mycmdout[1:]:
    full_size = (i.split()[4])
    myval =full_size.replace('%',' ')
    if int(myval) >=80:
        print(i.strip('\n'))
client.close()




# ------------------ in order to access windows machine from linux -------------
# we must enable openssh from win+r and then write   services.msc
# to create new user in windows --  win+r -- lusrmgr.msc


#!/usr/bin/python
import paramiko
hostname = '192.168.75.136'
username = 'zee'
password='zee123'

client =  paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd ="dir"

stdin, stdout, stderr =  client.exec_command(mycmd)

mycmdout = stdout.read().decode()

print(mycmdout)
client.close()


# --------------- file copying from remote machine -----------------

#this is the simple way to access remote machine 
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password   )
mycmd="df -h"

stdin, stdout, stderr = client.exec_command(mycmd)

mycmdout=stdout.read().decode()
print(mycmdout)
client.close()

#now to access file from remote server we use sftp 
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password   )

mysftp =  client.open_sftp()
print(mysftp)  #this will show paramiko sftp object

#### right not we are in windows machine 
#   window ip :   192.168.75.136
#   linux ip is : 192.168.241.204

#in order to get file from remote server we use get
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password   )

mysftp =  client.open_sftp()
mysftp.get('/home/zia/Documents/python_prac/server.csv' , 'server.csv')
mysftp.close()
client.close()


#now to send file from like from windows to linux 
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp =  client.open_sftp()
mysftp.put('server.csv' , 'server.csv') #here first is from where you send & 2nd arg where to send
mysftp.close()                          # but file will sent to /hom/user by defult 
client.close()

#now to send file to specific directory not at /home/username
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp =  client.open_sftp()
mysftp.chdir('/home/zia/Documents/python_prac')
mysftp.put('server.csv' , 'server.csv') 
mysftp.close()                        
client.close()


# to check your remote files from windows 

import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp =  client.open_sftp()
mysftp.chdir('/home/zia/Documents/python_prac')
print(mysftp.listdir())
mysftp.close()                        
client.close()

#to check details from files

import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp =  client.open_sftp()
mysftp.chdir('/home/zia/Documents/python_prac')
print(mysftp.stat('server.csv'))
mysftp.close()                        
client.close()

#to write in remote file 
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp =  client.open_sftp()
mysftp.chdir('/home/zia/Documents/python_prac')
file = mysftp.open('server.csv' , 'a')
file.write('this will be appended by z kayani')
mysftp.close()                        
client.close()


#now to read file 
import paramiko
hostname="192.168.241.204"
username="zia"
password= "zia123"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp =  client.open_sftp()
mysftp.chdir('/home/zia/Documents/python_prac')
file = mysftp.open('server.csv')
print(file.read())
mysftp.close()                        
client.close()

# ----- TASK -------------------
# you need to get free -g data from remote machine and store output into one file every days.

