#PROJECT ----------
I want to genrated Df -h output into CSV file then once CSV generated my python scrupt will pick the CSV file and import data into mysql database.


I want to create table 
table name : my_df_data
file_id
filesystem
size
used
avail
usage_with_per
mounted_on
datetime
ip_address
hostname


#We need to focus on bash commands
#I want to display df -h data without header 
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1'
udev                               953M     0  953M   0% /dev
/dev/mapper/ubuntu--vg-ubuntu--lv  8.9G  5.8G  2.7G  69% /
/dev/sda2                          875M  149M  665M  19% /boot

##################
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}'
udev 953M 0 953M 0% /dev
/dev/mapper/ubuntu--vg-ubuntu--lv 8.9G 5.8G 2.7G 69% /
/dev/sda2 875M 149M 665M 19% /boot

#now remove % sign 
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g'
udev 953M 0 953M 0 /dev
/dev/mapper/ubuntu--vg-ubuntu--lv 8.9G 5.8G 2.7G 69 /
/dev/sda2 875M 149M 665M 19 /boot

#now insert , between fields
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E "s/ +/,/g"
udev,953M,0,953M,0,/dev
/dev/mapper/ubuntu--vg-ubuntu--lv,8.9G,5.8G,2.7G,69,/
/dev/sda2,875M,149M,665M,19,/boot

#now insert date at end 
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E "s/ +/,/g" | sed "s/$/,$(date '+%F %T')/g"
udev,953M,0,953M,0,/dev,2022-10-02 11:15:40
/dev/mapper/ubuntu--vg-ubuntu--lv,8.9G,5.8G,2.7G,69,/,2022-10-02 11:15:40
/dev/sda2,875M,149M,665M,19,/boot,2022-10-02 11:15:40
root@abdeali:~/myproject#

#######################

#now insert ip address at end
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E "s/ +/,/g" | sed "s/$/,$(date '+%F %T')/g" | sed "s/$/,$(hostname -I | awk '{print $1}')/g"
udev,953M,0,953M,0,/dev,2022-10-02 11:17:02,192.168.1.8
/dev/mapper/ubuntu--vg-ubuntu--lv,8.9G,5.8G,2.7G,69,/,2022-10-02 11:17:02,192.168.1.8
/dev/sda2,875M,149M,665M,19,/boot,2022-10-02 11:17:02,192.168.1.8

##################
Final data 
root@abdeali:~/myproject# df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E "s/ +/,/g" | sed "s/$/,$(date '+%F %T')/g" | sed "s/$/,$(hostname -I | awk '{print $1}')/g" |  sed "s/$/,$(hostname)/g"
udev,953M,0,953M,0,/dev,2022-10-02 11:17:51,192.168.1.8,abdeali.local
/dev/mapper/ubuntu--vg-ubuntu--lv,8.9G,5.8G,2.7G,69,/,2022-10-02 11:17:51,192.168.1.8,abdeali.local
/dev/sda2,875M,149M,665M,19,/boot,2022-10-02 11:17:51,192.168.1.8,abdeali.local


OS falovur : root@abdeali:~/myproject# cat /etc/os-release | grep -iw "NAME" | awk -F = '{print $2}' | tr -d '"'
Ubuntu


################
#to find os name and then based on that apply will apply command df 
import os

try:
    os_name=os.popen("cat /etc/os-release | grep -iw \"NAME\" | awk -F = '{print $2}' | tr -d '\"'").read().strip('\n')
    if os_name == 'Ubuntu' or os_name == 'redhat':
        print(os_name)
    else:
        print("Other os found", os_name)
except Exception as e:
    print("Something having issue",e)


#######################
#now final code
import os
df_cmd=df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E \"s/ +/,/g\" | sed \"s/$/,$(date '+%F %T')/g\" | sed \"s/$/,$(hostname -I | awk '{print $1}')/g\" |  sed \"s/$/,$(hostname)/g"

try:
    os_name=os.popen("cat /etc/os-release | grep -iw \"NAME\" | awk -F = '{print $2}' | tr -d '\"'").read().strip('\n')
    if os_name == 'Ubuntu' or os_name == 'redhat':
        df_cmd=os.popen("df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E \"s/ +/,/g\" | sed \"s/$/,$(date '+%F %T')/g\" | sed \"s/$/,$(hostname -I | awk '{print $1}')/g\" |  sed \"s/$/,$(hostname)/g\"").read()
        print(df_cmd)
    else:
        print("Other os found", os_name)
except Exception as e:
    print("Something having issue",e)


#############################
We are converting data into csv file 
import os
try:
    os_name=os.popen("cat /etc/os-release | grep -iw \"NAME\" | awk -F = '{print $2}' | tr -d '\"'").read().strip('\n')
    if os_name == 'Ubuntu' or os_name == 'redhat':
        df_cmd=os.popen("df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E \"s/ +/,/g\" | sed \"s/$/,$(date '+%F %T')/g\" | sed \"s/$/,$(hostname -I | awk '{print $1}')/g\" |  sed \"s/$/,$(hostname)/g\" > myfilecsv.csv").read()
        print(df_cmd)
    else:
        print("Other os found", os_name)
except Exception as e:
    print("Something having issue",e)


root@abdeali:~/myproject# python3  python_csv_project.py

root@abdeali:~/myproject# ls -ltrh
total 8.0K
-rw-r--r-- 1 root root 601 Oct  2 11:30 python_csv_project.py
-rw-r--r-- 1 root root 250 Oct  2 11:30 myfilecsv.csv
root@abdeali:~/myproject# cat myfilecsv.csv
udev,953M,0,953M,0,/dev,2022-10-02 11:30:45,192.168.1.8,abdeali.local
/dev/mapper/ubuntu--vg-ubuntu--lv,8.9G,5.8G,2.7G,69,/,2022-10-02 11:30:45,192.168.1.8,abdeali.local
/dev/sda2,875M,149M,665M,19,/boot,2022-10-02 11:30:45,192.168.1.8,abdeali.local


###################################################################################3
#Now ltes intsert the data in database  and encripyt out password

#create a seperate file of commands like - mylinux.json
root@zeekayani:/home/Documents# cat mylinux.json 
{
        "username": "mysql_user",
        "password": "test123",
        "os_flavour": "cat /etc/os-release | grep -iw \"NAME\" | awk -F = '{print $2}' | tr -d '\"'",
        "df_cmd" : "df -h  | grep -v 'tmpfs' | awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E \"s/ +/,/g\" | sed \"s/$/,$(date '+%F %T')/g\" | sed \"s/$/,$(hostname -I | awk '{print $1}')/g\" |  sed \"s/$/,$(hostname)/g\" > myfilecsv.csv"
}

#now lets use that file instead of commands for better code visibility 
import os
import json

try:
    myjsonfile = "mylinux.json"
    with open(myjsonfile, "r") as jf:
        my_dict = json.load(jf)
        os_name = os.popen(my_dict['os_flavour']).read().strip('\n')
        if os_name == 'Ubuntu' or os_name == 'redhat':
            df_cmd = os.popen(my_dict['df_cmd']).read()
            print(df_cmd)
        else:
            print("Other os found", os_name)
except Exception as e:
    print("Something having issue", e)


###now we will create table in database
CREATE TABLE my_df_data (
    file_id INT(11) NOT NULL AUTO_INCREMENT,
    filesystem VARCHAR(255),
    size VARCHAR(255),
    used VARCHAR(255),
    avail VARCHAR(255),
    usage_with_per INT,
    mounted_on VARCHAR(255),
    datetime DATETIME,
    ip_address VARCHAR(255),
    hostname VARCHAR(255),
    PRIMARY KEY (file_id)
);

#now login with mysql user
mysql -u mysql_user -h 192.168.75.62 -pass

#use alnafi databse

#in this create the table with my_df_data name

#now insert manually values in this
INSERT INTO my_df_data 
(filesystem, size, used, avail, usage_with_per, mounted_on, datetime, ip_address, hostname) 
VALUES 
('/dev/sda2', '875M', '1:49M', '565M', 13, '/boot', '2022-10-02 13:14:05', '192.168.1.6', 'abdeal');



### now write a code for your password encryption and decryption
import json
from cryptography.fernet import Fernet

jsonfile = 'mypass.json'

# Load JSON data
with open(jsonfile) as jf:
    my_dict = json.load(jf)

# Display username and password
print("This is my username: " + my_dict['username'])
print("This is my Password: " + my_dict['password'])

mypass = my_dict['password']
print(mypass)

# Encrypt the password
message = mypass.encode("utf-8")
print("Encoded message:", message)

key = Fernet.generate_key()
print("Generated key:", key)

f = Fernet(key)
print("Fernet object:", f)

encrypted = f.encrypt(message)
print("Encrypted password:", encrypted)

# Decrypt the password
decrypted = f.decrypt(encrypted)
print("Decrypted bytes:", decrypted)

my_new_pass = decrypted.decode("utf-8")
print("Decrypted password:", my_new_pass)






