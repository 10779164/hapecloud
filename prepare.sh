!/bin/bash

#bash font color
red='\033[0;31m'
green='\033[0;32m'
NC='\033[0m'

. /etc/os-release

if echo $ID | grep -iq "centos"; then
        yum install epel-release python-pip MySQL-python mariadb-server -y
	pip install uwsgi 
        mkdir -p /data/flask_data
        echo -e "${green}done${NC}"

elif echo $ID | grep -iq "debian"; then
        apt-get install libmysqlclient-dev python-dev python-pip mysql-server -y
        pip install MySQL-python uwsgi
        mkdir -p /data/flask_data
        echo -e "${green}done${NC}"

elif echo $ID | grep -iq "ubuntu"; then
        apt-get install libmysqlclient-dev python-dev python-pip mysql-server -y
        pip install MySQL-python uwsgi
        mkdir -p /data/flask_data
        echo -e "${green}done${NC}"

else
        echo -e "${red}不想写太多系统版本的判断，请使用centos/ubuntu的系统${NC}"
        exit 0
fi



