#!flask/bin/python

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../..")))

from app import db
from app.models import Requests

def create_entry():

		request = Requests(0)
		db.session.add(request)
		db.session.commit()

create_entry()
