### About the Tech Stack

- Psycopg2 - this gives the ability to connect to a postgres server using Python

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
