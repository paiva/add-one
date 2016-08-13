from app import app, db
from sqlalchemy import Column, Integer, String, ForeignKey
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class User(db.Model,UserMixin):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	num_requests = db.Column(db.Integer, default='0', index=True, unique=True)

if __name__ == 'main':
	manager.run()
