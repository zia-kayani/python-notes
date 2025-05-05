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