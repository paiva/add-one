# Add One

Prototype of multiple applications talking to the same database implementing the Flask framework. The only purpose of the application is to add 1 (+1) to the number of requests done to the server.

### Installation
---

First, install dependencies with `pip install -r requirements.txt` and make sure
you have a postgres database server installed on your machine.  

**Step 1:** Create postgres database in localhost called `add_one`

     psql -d postgres
     create database add_one
     \q

**Step 2:** Create database entries and migration

     cd /scripts/db
     python db_create.py
     python db_upgrade.py
     python db_populate.py

**Step 3:** Run application on localhost (port 5000 by default)

     python run.py


Then, click on button `+1` to add a server request.
