from app import app, db
from sqlalchemy import Column, Integer, String, ForeignKey
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

class Requests(db.Model):
	__tablename__ = 'requests'
	id = db.Column(db.Integer, primary_key=True)
	num_requests = db.Column(db.Integer, index=True)

	def __init__(self, num_requests):
		self.num_requests = num_requests
