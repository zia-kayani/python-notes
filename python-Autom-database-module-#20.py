#------ Database Module -----------

# -- install sql-server -----
#step1:- #apt-get update
#step2:- apt-get install mysql-server
#step3:- 
# systemctl status mysql.service
# systemctl enable mysql.service
# systemctl start mysql.service
#step4:- #Now you need to confiugre your mysql server
# mysql_secure_installation
#step5-: login
# mysql -u root -p

#to check database   show databases;
#to create database   create database <db_name>;

#to create the databse , like here alnafi
create database alnafi;

#to show all databases
show databases;

#to use this alnafi database
use alnafi;

#to show all tables
show tables;

#to create table in this db
create table trainer_details
(
t_id int NOT NULL AUTO_INCREMENT,
fname char(255),
lname char(255),
desig char(255),
username varchar(255),
password varchar(255),
salary int(255),
datetime datetime,
PRIMARY KEY (t_id)
);

# to see the table structure,
describe trainer_details;

#to insert record in this table
insert into trainer_details (fname,lname,desig,username,password,salary,datetime) 
values ('Abdeali','Dodiya','Software Developer','abd','abd123',1000,'2022-10-01');

#to see the table contetn
select * from trainer_details;

#to see specific column 
select fname,lname,desig from trainer_details;

#to see the details about specific user
select fname,lname,desig from trainer_details where fname='Abdeali';

#to see details based on id
select * from trainer_details where t_id=1;

#to see the details based on condition

#to add column in existing table 
alter table trainer_details add column email varchar(255);

#how to delete any column in your table;
alter table trainer_details DROP column email;

#how to add column after existing table column
alter table trainer_details add email varchar(255) after password;

#add another column 
insert into trainer_details (fname,lname,desig,username,password,salary,datetime) 
values ('Sarah','shaikh','FD','sarah','sarah123',3000,'2022-10-02');

#how to update your data from mysql
 update trainer_details set password='sarah@123' where t_id=3;

#howt odelete your row from mysql
delete from trainer_details where t_id=3;

#We will insert another data
insert into trainer_details (fname,lname,desig,username,password,salary,datetime) 
values ('Sarah','shaikh','FD','sarah','sarah@123',3000,'2022-10-02');

#describe 
desc trainer_details;


#-------------python module with database - ---
#we use tool like mysql-connector to remotely access our databse

#to install mysql-connector on Windows
#pip installl mysql-connector 
#now open python shell -- python
#now hit this  -- import mysql.connector -- if no error means installed

#to install mysql-connector on Linux
#pip3 install  mysql-connector
#now  -- python3
#import mysql.connector



#CODE
#
import mysql.connector
mydb =  mysql.connector.connect(host='localhost',user='root',password='zia123',database='alnafi')
#mysql connection object create
cur =  mydb.cursor()

#Fetching data
sql = '''select * from trainer_details'''

#now execute
cur.execute(sql)

result = cur.fetch()

mydb.close()
#in the above, script has no issue but there will be an error in the output while connecting to mysql
# You will get below error 
# mysql.connector.errors.ProgrammingError: 1698 (28000): Access denied for user 'root'@'localhost'




#now -to fix the error 
#login to mysql with root 
## create mysql_user then you can access from myscript 
create user 'mysql_user'@'%'IDENTIFIED BY 'test123';

#now when you login with this user, will not be allowed
root@abdeali:~/lect55# mysql -u mysql_user -p
Enter password:
ERROR 1045 (28000): Access denied for user 'mysql_user'@'localhost' (using password: YES)
 
 #with ip address , we are allowd - means with localhost its not allowing
 root@abdeali:~/lect55# mysql -u mysql_user  -h 192.168.75.63  -p
Enter password:
Welcome to the MySQL monitor.

#now you need to open one file and edit with below line 

vim /etc/mysql/mysql.conf.d/mysqld.cnf
bind-address            = localhost
#you need to change value tih 0.0.0.0

bind-address            = 0.0.0.0

:wq!

#now systemctl restart mysql

#now after creating the user run the programm
import mysql.connector
mydb= mysql.connector.connect(host="192.168.1.8",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = ''' select * from trainer_details '''
cur.execute(sql)
result = cur.fetch()
mydb.close() 
#You will get follow error --
#mysql.connector.errors.ProgrammingError: 1044 (42000): 
# Access denied for user 'mysql_user'@'%' to database 'alnafi'

#means this user has no privilages to access the database 
# Now we will provide fulll access to mysql_user - from root user
mysql> grant all on *.* to 'mysql_user'@'%' WITH GRANT OPTION;

#now user has privilages, we can even login
mysql -u mysql_user -h 192.168.1.8 -p
#can see all databases which were in root user  -- show databses;

#now finally we can update our query - that will run successfull 
import mysql.connector
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = ''' select * from trainer_details '''
cur.execute(sql)
result = cur.fetchall()
print(result)
mydb.close()



# -----------now remote data insertion ---------

#to get user1 details - i am runnin all below from remote machine
import mysql.connector
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = ''' select * from trainer_details where t_id=1'''
cur.execute(sql)
result = cur.fetchall()  # fetchone() will fetch only frist record from table
print(result)
mydb.close()


#fetching all the data 
import mysql.connector
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = ''' select * from trainer_details '''
cur.execute(sql)
result = cur.fetchall()  
for i in result:
    print(result)
mydb.close()

#data insertion 
import mysql.connector
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = """ insert into trainer_details (fname,lname,desig,username,password,salary,datetime) values ('Arwa','dodia','Blogger','arwa','arwa123',4000,'2022-10-02') """
cur.execute(sql)
mydb.commit()
mydb.close()

#now to insert dynamic data 
import mysql.connector
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = "insert into trainer_details (fname,lname,desig,username,password,salary,datetime) values (%s,%s,%s,%s,%s,%s,%s) "
data = ('Zoya','Ukani','SME','zaoya','zoya123','8000','2022-10-02')
cur.execute(sql,data)
mydb.commit()
mydb.close()


#I want to insert data as datetime object via fix variable 
import mysql.connector
from datetime import *

time =  datetime.now()
mycustom = time.strftime("%Y-%m-%d %H:%M:%S")
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
sql = "insert into trainer_details (fname,lname,desig,username,password,salary,datetime) values (%s,%s,%s,%s,%s,%s,%s) "
data = ('Ali','Patel','Devops','ali','ali123','7000',mycustom)
cur.execute(sql,data)
mydb.commit()
mydb.close()

#We are update data via python
import mysql.connector
from datetime import *

time =  datetime.now()
mycustom = time.strftime("%Y-%m-%d %H:%M:%S")
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
data="zoya"
sql = " update trainer_details set username="+data+ " where t_id=6"
cur.execute(sql)
mydb.commit()
mydb.close()  #this program will generate an error 
#error will be like this : mysql.connector.errors.ProgrammingError: 1054 (42S22): Unknown column 'zoya' in 'field list'


#to get rid of above error 
import mysql.connector
from datetime import *

time =  datetime.now()
mycustom = time.strftime("%Y-%m-%d %H:%M:%S")
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
data="'zoya'"
sql = " update trainer_details set username="+data+ " where t_id=6"
cur.execute(sql)
mydb.commit()
mydb.close()


# Update data with select query 
import mysql.connector
from datetime import *

time=datetime.now()
mycustom = time.strftime("%Y-%m-%d %H:%M:%S")
mydb= mysql.connector.connect(host="192.168.75.63",user="mysql_user",password="test123",database="alnafi")
cur = mydb.cursor()
data="'zoya@123'"
sql = " update trainer_details set password="+data+ " where t_id=6"

cur.execute(sql)
mydb.commit()
select_sql = """ select * from trainer_details """
cur.execute(select_sql)
result = cur.fetchall()
for data in result:
    print(data)

mydb.close()


#to delete data
sql = " delete from trainer_details where fname="+mydata



