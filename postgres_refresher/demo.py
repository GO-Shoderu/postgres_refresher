import psycopg2     #importing the package for communicating with the database

# establishing connection with the database
connection = psycopg2.connect('dbname=example')

# creating cursor to queue up work in transactions
cursor = connection.cursor()

# beginning of transaction

# creating a table
cursor.execute('''
    CREATE TABLE usernames (
        id INTEGER PRIMARY KEY,
        names VARCHAR NOT NULL
    );
''')

# inserting into a newly created table
cursor.execute('''
    INSERT INTO usernames (id, names) VALUES (1, 'GO.Shoderu');
''')

connection.commit()

connection.close()
cursor.close()

# ended the transaction
