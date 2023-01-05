**This repo of mine is for refreshing my memory on Postgres and it's related libraries on python**

### General Installation Requirements

You can follow the links below for installation/setup of Postgres

- [Installation and Setup](https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04)
- [Creating a Postgres User](https://phoenixnap.com/kb/postgres-create-user)
- [Creating roles and managing permissions](https://www.digitalocean.com/community/tutorials/how-to-use-roles-and-manage-grant-permissions-in-postgresql-on-a-vps-2) (make sure you give your user a superuser role)

### About the Tech Stack

- Flask - this is a library, it is going to be the web-server framework of my choice
- Psycopg2 - this gives the ability to connect to a postgres server using Python
- SQLAlchemy - like Psycopg2 but helps with connecting to a Flask application
- Flask-SQLAlchemy - this is a flask extension for SQLAlchemy to easily work with SQLAlchemy and a flask application

### Psycopg2, SQLAlchemy & Flask-SQLAlchemy

_All these helps connect the postgres database to a Flask application_
