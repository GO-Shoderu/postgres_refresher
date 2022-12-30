### About the Tech Stack

- Flask - this is a library, it is going to be the web-server framework of my choice
- Psycopg2 - this gives the ability to connect to a postgres server using Python
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
- on your browser enter 127.0.0.1:5000 or localhost:5000, the webpage should say `Hello World!`
