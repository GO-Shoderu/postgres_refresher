This is a dummy app transfering information from information from the server to the client using a templating engine called Jinja

This particular project folder touches on the R part of the CRUD (Create, Read, Update and Delete)

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

- run `createdb todoapp` on your terminal
- run `psql todoapp` on a new tab in your terminal
- run `insert into todos (description) values ('what ever string you want');`
- you can add as many todos as possible
- run `select * from todos;`
- run `python3 app.py` on your terminal

```
todoapp=# select * from todos;
 id |         description
----+-----------------------------
  1 | study for AWS certification
  2 | watch fullstack videos
  3 | watch more editing videos
  4 | work on alx project
(4 rows)

```

- on your browser enter 127.0.0.1:5000 or localhost:5000, the webpage should list out all the descriptions from the database
