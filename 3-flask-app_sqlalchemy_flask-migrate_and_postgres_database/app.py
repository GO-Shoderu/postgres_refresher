from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)   #initializing the app

# creating a link to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        #silencing any deprecation warnings

# linking an instance of the dabase to the flask app
db = SQLAlchemy(app)

"""
this will help use flask-migrate database commands to begin
initializing migrations, upgrading, downgrading and generating migrations
"""
migrate = Migrate(app, db)

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
    completed = db.Column(db.Boolean, nullable=False, default=False)

    # for debugging purposes using python
    def __repr__(self):
        return f'<Todo id: {self.id}, description: {self.description}, completed: {self.completed}>'

@app.route('/')
def index():
    todo = Todo.query.first()
    return "You have to " + todo.description + "!!!"

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3000)
