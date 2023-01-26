import sys
from flask import Flask, render_template, request, jsonify, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   #initializing the app

# creating a link to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/todoapp'     #catering for windows operating system
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        #silencing any deprecation warnings

# linking an instance of the dabase to the flask app
db = SQLAlchemy(app)
"""
db = SQLAlchemy(app, session_options={"expire_on_commit": False})
having the expire on commit option can be set to false in order to be able to do session close or roll backs when necessary
but because this has some side effect I will be using abort in place of this for error handling
"""

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
        return f'<Person id: {self.id}, description: {self.description}, completed: {self.completed}>'

# this won't be needed anymore if flask-migrate is used
db.create_all()     #creates the table based on the db.Model that was configured with the associated table

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    # creating transactions
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    #end of transactions

    if error:
        abort (400)
    else:
        return jsonify(body)

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    error = False
    body = {}
    # creating transactions
    try:
        completed = request.get_json()['completed']
        print('completed', completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.add(todo)
        db.session.commit()
        body['completed'] = todo.completed
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    #end of transactions

    if error:
        abort (400)
    else:
        return redirect(url_for('index'))

@app.route('/todos/<todo_id>/delete-todos', methods=['DELETE'])
def delete_todo(todo_id):
    error = False
    # creating transactions
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    #end of transactions

    if error:
        abort (400)
    else:
        print("Todo deleted")
        return jsonify({'success': True})

# this is another option for compiling

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

# this will require a shorter terminal command (python3 app.py)
