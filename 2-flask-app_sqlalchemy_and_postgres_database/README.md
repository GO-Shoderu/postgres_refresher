### About the Tech Stack

- Flask - this is a library, it is going to be the web-server framework of my choice
- SQLAlchemy - like Psycopg2 but helps with connecting to a Flask application
- Flask-SQLAlchemy - this is a flask extension for SQLAlchemy to easily work with SQLAlchemy and a flask application

### Psycopg2, SQLAlchemy & Flask-SQLAlchemy

_All these helps connect the postgres database to a Flask application_

### Required Installation

- Python
- Pip
- Flask
  run `pip3 install flask` or `pip install flask`
- Flask-SQLAlchemy
  run `pip3 install flask-sqlalchemy` or `pip install flask-sqlalchemy`

### Instructions for running the code and seeing output

- run `FLASK_APP=flask-hello-app.py flask run` on your terminal
- run `psql example` on a new tab in your terminal
- run `\dt` to be sure the table `persons` was successfully created as shown below

```
salt@salt:~/Desktop/sql_prep/2-flask-app_and_postgres_database$ psql example
psql (15.1 (Ubuntu 15.1-1.pgdg22.04+1))
Type "help" for help.

example=# \dt
           List of relations
 Schema |   Name    | Type  |  Owner
--------+-----------+-------+----------
 public | persons   | table | postgres
 public | table1    | table | salt
 public | usernames | table | salt
(3 rows)
```

- run `insert into persons (name) values ('Gabriel')` to insert into the database table
- on your browser enter 127.0.0.1:5000 or localhost:5000, the webpage should say `Hello Gabriel, you have successfully made a connection to the database!!!`
