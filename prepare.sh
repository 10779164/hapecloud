#!/bin/bash

#bash font color
red='\033[0;31m'
green='\033[0;32m'
NC='\033[0m'

. /etc/os-release

if echo $ID | grep -iq "centos"; then
	yum install epel-release python-pip -y &>/dev/zero
	mkdir -p /data/flask_data               
	echo -e "${green}done${NC}"
else
	echo -e "${red}不想写太多系统版本的判断，请使用centos的系统(内核版本>=3.10)${NC}"
	exit 0
fi


~
