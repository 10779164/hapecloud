from flask import Flask
app=Flask(__name__)
app.config['SECRET_KEY']="wobuhuigaosunizhejiushisecretkey"
from main import views
from user import views
