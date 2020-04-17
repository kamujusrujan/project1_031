from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
class User(db.Model):
	__tablename__ = 'registeredUsers'
	mail = db.Column(db.String,primary_key = True)
	name = db.Column(db.String)
	password = db.Column(db.String)
	created_data  = db.Column(db.DateTime, default = datetime.datetime.utcnow)
