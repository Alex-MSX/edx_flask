from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    text = "Mi primer página con Flask!!!"
    return render_template("index.html", headline=text)
