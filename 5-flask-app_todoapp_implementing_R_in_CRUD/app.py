from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   #initializing the app

# creating a link to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
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
class Todo(db.Model):
    #this is optional for specifying the name of the table by default it takes the name of the class Person
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    # for debugging purposes using python
    def __repr__(self):
        return f'<Person id: {self.id}, description: {self.description}>'

db.create_all()     #creates the table based on the db.Model that was configured with the associated table

@app.route('/')
def index():
    return render_template('index.html', data = Todo.query.all())


# this is another option for compiling

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

# this will require a shorter terminal command (python3 app.py)
