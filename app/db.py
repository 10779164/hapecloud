import MySQLdb

class db():
    def __init__(self):
    	self.user="hapecloud"
    	self.passwd="hapecloudadmin"
    	self.database="Hapecloud"
    
    def conn(self):
	conn=MySQLdb.connect(user=self.user,passwd=self.passwd,host='localhost',charset='utf8')
	conn.select_db(self.database)
	return conn

    def cur(self):
	conn=MySQLdb.connect(user=self.user,passwd=self.passwd,host='localhost',charset='utf8')
	conn.select_db(self.database)
	cur=conn.cursor()
	return cur
  	
###create database
#create database Hapecloud charset utf8;

###create database user
#grant all privileges on Hapecloud.* to hapecloud@'%' identified by 'hapecloudadmin';

###create user table
#create table user(id smallint(6) auto_increment unique key,user varchar(10) primary key,password varchar(20) not null,level smallint(6),register_time varchar(20),last_login varchar(20));

###create admin user
#insert into user value('','admin','123.com',9,'2018-10-27 17:58:12','192.168.80.1');
