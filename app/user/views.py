#encoding=utf8
import time
import commands
from .. import db
import flask
from app import app
from flask import render_template,request,url_for,session,request,flash,redirect


@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
	username = request.form.get('username')
	password = request.form.get('password')
	level=0
	register_time = time.strftime('%Y-%m-%d %H:%M:%S')
	last_login = request.remote_addr
	query_user_sql=("select user from user where user='%s'") % username
	sql=("insert into user values(NULL,'%s','%s','%d','%s','%s')") % (username,password,level,register_time,last_login)
	mysql=db.db()
        conn=mysql.conn()
	cur=conn.cursor()
 
	cur.execute(query_user_sql)
	row=cur.fetchone()
	if row == None:
	    try:
            	cur.execute(sql)
	    	conn.commit()
	    	dir="/data/flask_data/"+username
	    	create_userdir_cmd="mkdir -p "+dir
	    	commands.getoutput(create_userdir_cmd)
	    	return '注册成功！<a href="/" style="color:red">返回登录页面</a>'
	    except Exception,e:
	    	conn.rollback()
	    	return "<span style='color:red;'>注册失败： </span>"+str(e)
		cur.close()
		conn.close()
	else:
	    return "<span style='color:red;'>Error:</span>用户--"+username+"--已存在"
    else:
	return render_template('signin.html')
