from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   #initializing the app

# creating a link to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        #silencing any deprecation warnings

# linking an instance of the dabase to the flask app
db = SQLAlchemy(app)

# bypassing a weird error with this
app.app_context().push()

"""
creating a table using SQLAlchemy
creating a Person class and inheriting from db.Model
through the help of SQLAlchemy mapping functionality
"""
class Person(db.Model):
    #this is optional for specifying the name of the table by default it takes the name of the class Person
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # for debugging purposes using python
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()     #creates the table based on the db.Model that was configured with the associated table

@app.route('/')
def index():
    person = Person.query.first()
    return "Hello " + person.name + ", you just successfully made a connection to the database!!!"

"""
# this is another option for compiling

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3000)

# this will require a shorter terminal command (python3 flask_hello_app.py)

"""
