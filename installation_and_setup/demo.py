import psycopg2     #importing the package for communicating with the database

# establishing connection with the database
connection = psycopg2.connect('dbname=example')

# creating cursor to queue up work in transactions
cursor = connection.cursor()

# beginning of transaction

# making sure the table is dropped if it exist
cursor.execute('DROP TABLE IF EXISTS usernames;')

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

# other ways of making this work using different variations of string composition
# using turples
cursor.execute('''
    INSERT INTO usernames (id, names) VALUES (%s, %s);
''', (2, 'Gabriel'))

# using dictionary
query = 'INSERT INTO usernames (id, names) VALUES (%(id)s, %(names)s);'

data = {
    'id': 3,
    'names': 'Shoderu'
}

cursor.execute(query, data)

connection.commit()

connection.close()
cursor.close()

# ended the transaction
