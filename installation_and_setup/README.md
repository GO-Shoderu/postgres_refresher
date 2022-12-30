### Installation Requirements

You can follow the links below for installation/setup of Postgres

- [Installation and Setup](https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04)
- [Creating a Postgres User](https://phoenixnap.com/kb/postgres-create-user)
- [Creating roles and managing permissions](https://www.digitalocean.com/community/tutorials/how-to-use-roles-and-manage-grant-permissions-in-postgresql-on-a-vps-2) (make sure you give your user a superuser role)

### Creation of required database

After ensuring the proper installation of postgres
run `createdb example` on your terminal

### Code execution

After the creation of the database
run `python3 demo.py` on your terminal

### Checking for successful code execution

To check if the code ran successfully

- run `psql example` on your terminal to connect to the database
- run `\dt` on your terminal and be sure that the table **usernames** is listed as one of the response
- run `select * from usernames;` on your terminal to be sure the names you inserted are in the database as shown below

```
example=# select * from usernames;
 id |   names
----+------------
  1 | GO.Shoderu
  2 | Gabriel
  3 | Shoderu
(3 rows)

```
