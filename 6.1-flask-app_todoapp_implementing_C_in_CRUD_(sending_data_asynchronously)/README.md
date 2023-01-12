This is a dummy app transfering information from information from the server to the client using a templating engine called Jinja

This particular project folder touches on the C part of the CRUD (Create, Read, Update and Delete)
Data will be sent to the server asynchronously with the help of AJAX.

### About the Tech Stack

- Flask - this is a library, it is going to be the web-server framework of my choice
- SQLAlchemy - like Psycopg2 but helps with connecting to a Flask application
- Flask-SQLAlchemy - this is a flask extension for SQLAlchemy to easily work with SQLAlchemy and a flask application
- Ajax - allows web pages to be updated fast through asynchronously exchanging small amounts of data back and forth with the server. It allows only a part of a web page to be updated without reloading the entire page.

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
- you can add as many todos as possible from the web interface
- run `select * from todos;` on your terminal to see newly created todos
- run `python3 app.py` on your terminal

```
todoapp=# select * from todos;
 id |                  description
----+-----------------------------------------------
  1 | study for aws certification
  2 | watch fullstack videos
  3 | watch more editing videos
  4 | work on alx project
  5 | help Matshepo with python
  6 | do some meditation
  7 | call family
  8 | write what needs to be done tomorrow
  9 | remember to work on Tutu's design as promised
 10 | get enough sleep
(10 rows)

```

- on your browser enter 127.0.0.1:5000 or localhost:5000, the webpage should list out all the descriptions from the database
