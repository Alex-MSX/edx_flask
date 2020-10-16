from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

#Para correr el código "env FLASK_APP=hello.py flask run"

@app.route("/david")
def david():
    return "Hello, David!!"

@app.route("/maria")
def maria():
    return "Hello, María"

@app.route("/<string:name>")
def hello(name):
    return "Hello, {}!".format(name.capitalize())
