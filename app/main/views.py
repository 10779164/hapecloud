#encoding=utf8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import commands
import flask 
from app import app 
from flask import render_template,request,url_for,send_file,send_from_directory,jsonify,redirect,session
#from app.forms import LoginForm,RegistForm
from werkzeug import secure_filename
from .. import db 

def get_file_desc():
    files_list=[]
    dir = '/data/flask_data/'+session.get('username')
    for file in os.walk(dir):
    	files_list.append(file)

    files_list=files_list[0][2]
    file_desc=[]

    for file in files_list:
    	dict={}
    	#filename
    	file_name=file
    	dict['file_name']=file_name

    	#filesize
    	file_size_cmd='du -sh'+' '+dir+'/'+file_name+'|'+"awk '{print $1}'"
    	file_size=commands.getoutput(file_size_cmd)
    	dict['file_size']=file_size

    	#file createtime
    	file_createtime_cmd='stat'+' '+dir+'/'+file_name+'|'+"grep Access | grep -v Uid | awk -F'.' '{print $1}' | awk '{print $2,$3}'"
    	file_createtime=commands.getoutput(file_createtime_cmd)
    	dict['file_createtime']=file_createtime

        file_desc.append(dict)

    return file_desc


@app.route('/',methods=('GET','POST'))
@app.route('/login',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('password')
	sql = "select user,password from user where user=%s and password=%s"
	mysql = db.db()
	cur = mysql.cur()
 	cur.execute(sql,(username,passwd))
	row=cur.fetchone()
        if row != None:
            session['username']=username
            session['passwd']=passwd
            session.permanent = True
            return redirect(url_for('disk'))
        else:
	    error="用户名或者密码验证失败!"
            return render_template('index.html',error=error)
    else:
        return render_template('index.html',error='')


@app.route('/forget_passwd')
def forget_passwd():
    return render_template('forget_passwd.html')


@app.route('/disk')
def disk():
    if 'username' in session:
	user=session.get('username')
	file_desc=get_file_desc()
        return render_template('disk.html',result=file_desc,user=user)
    else:
        return redirect(url_for('index'))


@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        #print '\n'.join(['%s:%s' % item for item in request.__dict__.items()])
        try:
            #starttime=time.time()
            f = request.files['filename']
	    #print f.filename.replace(' ','')
	    dir='/data/flask_data/'+session.get('username')
            upload_path=os.path.join(dir,f.filename.replace(' ',''))
            f.save(upload_path)
            #endtime=time.time()
            #real_time=float('%0.2f' % (endtime-starttime))
            #command="du -sh "+dir+'/'+f.filename+"| awk '{print $1}'"
            #file_size=commands.getoutput(command)
            #result='文件"'+f.filename+'"上传成功'
            #f.save(os.path.join(app.config['file_path'],'/',secure_filename(f.filename))
            return redirect(url_for('disk'))
            #return render_template('disk.html',result=result,file_size='文件大小：'+file_size,time='上传耗时：'+str(real_time)+'s')
        except Exception,e:
            #result="文件上传失败："+str(e)
            #return render_template('disk.html', result=result)
	    return str(e)
    else:
        #return render_template('disk.html',result='')
	return redirect(url_for('disk'))


@app.route('/delete',methods=['POST'])
def delete_file():
    dir="/data/flask_data/"+session.get('username')
    dict=request.form.to_dict()
    for filename in dict:
	filename=filename
    #print filename
    delete_file_cmd="rm -f "+dir+'/'+filename
    try:
    	commands.getoutput(delete_file_cmd)
    	return redirect(url_for('disk'),code=301)
     	#return render_template('disk.html')
    except Exception,e:
	return "unkown error"


@app.route('/download/<filename>',methods=['GET'])
def download_file(filename):
    try:
	dir="/data/flask_data/"+session.get('username')
    	return send_from_directory(dir, filename, as_attachment=True)
	#return redirect(url_for('disk'))
    except Exception,e:
	abort(404)

@app.route('/test', methods=["GET","POST"])
def test():
    dir="/data/flask_data/"
    filename='1.jpg'
    return send_from_directory(dir, filename, as_attachment=True)
    #return send_file(filename=filename, as_attachment=True)
    #return "flask-login"

