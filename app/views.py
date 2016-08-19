from app import app
from flask import render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from .models import Requests

db = SQLAlchemy(app)

@app.route("/")
def index():
	return render_template('homepage/index.html')

@app.route('/add_one', methods=['GET','POST'])
def add_one():
	if request.method == 'POST':
		requests = db.session.query(Requests).one()
		print(requests.num_requests)
		requests.num_requests = requests.num_requests + 1
		print(requests.num_requests)
		db.session.commit()

		return redirect(url_for('index'))
