#mysql -uroot -p < hapecloud.sql
###create database
create database Hapecloud charset utf8;

###create database user
grant all privileges on Hapecloud.* to hapecloud@'%' identified by 'hapecloudadmin';

###create user table
use Hapecloud;
create table user(id smallint(6) auto_increment unique key,user varchar(10) primary key,password varchar(20) not null,level smallint(6),register_time varchar(20),last_login varchar(20));

