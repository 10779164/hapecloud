# hapecloud

搭建步骤

1.git clone https://github.com/10779164/hapecloud.git

2.进入到项目目录，执行准备脚本 bash prepare.sh

3.安装flask环境 pip install -r requirements.txt

5.导入sql文件，mysql -uroot -p < hapecloud.sql

4.安装nginx
配置文件：
server {
    listen 80;
    server_name hapecloud.jouline.com;
    charset     utf-8;
    client_max_body_size 512M;
 
    location / {
        include uwsgi_params;
        #uwsgi_pass unix:/root/hapecloud/uwsgi.sock;
	uwsgi_pass 127.0.0.1:5000;
    }
	access_log  /var/log/hapecloud/access.log;
        error_log  /var/log/hapecloud/error.log;
}


5.运行uwsgi
uwsgi --ini uwsgi.ini

6.重新加载nginx
nginx -s reload

