import os
from functools import wraps

from flask import Flask, session,render_template,request,url_for,redirect
import random 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from database import *

app = Flask(__name__)
app.secret_key = 'srujan_123'



app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:srujan@localhost:5432/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'log' not in session :
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function



@app.route("/") 
def index():
    db.create_all()
    if 'log' in session :
        return render_template('mainpage.html',name = session['name'])
    return render_template('mainpage.html', name = '')
   


@app.route('/login', methods = ['GET','POST'])
def login():
    if(request.method == 'GET'):
        return render_template('loginpage.html')
    mail,password = (request.form.get('mailid'), request.form.get('password'))
    u = User.query.filter_by(mail = mail).first()
    if u.password == password:
        session['log'] = True
        session['name'] = u.name
        return render_template('success.html',mail=mail)
    else:
        return render_template('loginpage.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return 'dashboard'



@app.route('/register', methods = ['GET','POST'])
def register():
    if (request.method == "GET"):
        return render_template('registerpage.html')

    mail,password = (request.form.get('mailid'), request.form.get('password'))
    db.session.add(User(mail = mail, name = mail.split('@')[0],password = password))
    db.session.commit()
    session['log'] = True
    return render_template('success.html',mail=mail)



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('dashboard'))



@app.route('/admin')
def admin():
    userlist= User.query.order_by(User.created_data).all()

    return render_template('admin.html',list = userlist)
