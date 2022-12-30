from flask import Flask

app = Flask(__name__)   #initializing the app

@app.route('/')
def index():
    return "Hello World!"
