import db
import time

a=db.db()
conn=a.conn()
cur=a.cur()
username="test"
password="123.com"
level=0
register_time = time.strftime('%Y-%m-%d %H:%M:%S')
last_login = "192.168.80.1"
print conn
print cur
#sql=("insert into user values(NULL,'%s','%s','%d','%s','%s')") % (username,password,level,register_time,last_login)
sql="insert into user value(NULL,'test22','123.com',0,'2018-10-27 19:58:12','192.168.80.1')"
try:
    cur.execute(sql)
    #row = cur.fetchall()
    #for i in row:
	#print i
    conn.commit()
    #cur.close()
except Exception,e:
    print e
    conn.rollback()

cur.close()
conn.close()
print "haha"

