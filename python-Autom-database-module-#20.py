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





