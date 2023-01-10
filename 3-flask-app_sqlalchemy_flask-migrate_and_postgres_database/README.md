### About the Tech Stack

- Flask - this is a library, it is going to be the web-server framework of my choice
- SQLAlchemy - like Psycopg2 but helps with connecting to a Flask application
- Flask-SQLAlchemy - this is a flask extension for SQLAlchemy to easily work with SQLAlchemy and a flask application
- Flask-Migrate - this is a flask extension for SQLAlchemy to make sure the data within a database isn't lost when changes to database schema erupt

### Psycopg2, SQLAlchemy & Flask-SQLAlchemy

_All these helps connect the postgres database to a Flask application_

### Required Installation

- Python
- Pip
- Flask
  run `pip3 install flask` or `pip install flask`
- Flask-SQLAlchemy
  run `pip3 install flask-sqlalchemy` or `pip install flask-sqlalchemy`
- Flask-Migrate
  run `pip3 install Flask-Migrate` or `pip install Flask-Migrate`

### Flask-Migrate commands

- `flask db init`
  this creates the initial migrations directory structure in the project directory
- `flask db migrate`
  this detects the model changes to be made and craetes a migration file with upgrade and downgrade logic set up. (this replaces the use of db.create_all()). This is to be executed after every changes to the database schema for instance, like adding a new column to a database table
- `flask db upgrade`
  runs the upgrade command in the migration file in order to apply the migration. It upgrades to the latest version of unapplied migrations
- `flask db downgrade`
  runs the downgrade command in the migration file in order to roll back the migration

### Instructions for running the code and seeing output

- run `python3 app.py` on your terminal
- run `createdb todoapp` on your terminal
- run `psql todoapp` on a new tab in your terminal
- run `insert into todos (description) values ('what ever string you want');`
- you can add as many todos as possible
- run `select * from todos;`

#### before migration

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

#### after migration

```
psql todoapp
psql (15.1 (Ubuntu 15.1-1.pgdg22.04+1))
Type "help" for help.

todoapp=# select * from todos;
 id |         description         | completed
----+-----------------------------+-----------
  1 | study for AWS certification | f
  2 | watch fullstack videos      | f
  3 | watch more editing videos   | f
  4 | work on alx project         | f
(4 rows)

```

- on your browser enter 127.0.0.1:5000 or localhost:5000, the webpage should say `Hello Gabriel, you have to study for AWS certificaation!!!`
