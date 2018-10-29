#!/usr/bin/python
#encoding=utf8
from flask import Flask
app = Flask(__name__)

#app.debug = True  定义在此无效？？？
#import config
from app import app
app.debug = True
#app.config.from_object(config)

app.run(host='0.0.0.0',port=80,threaded='True')
