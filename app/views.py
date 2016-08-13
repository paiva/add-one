from app import app
from flask import render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from .models import User

db = SQLAlchemy(app)

@app.route("/")
def index():
	return render_template('homepage/index.html')

@app.route('/add_one', methods=['GET','POST'])
def add_one():

	if request.method == 'POST':
		user = db.session.query(User).filter(User.num_requests)

		user.num_requests += 1
		session.commit()
