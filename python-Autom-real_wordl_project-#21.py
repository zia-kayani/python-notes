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


