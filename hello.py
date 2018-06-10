from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/Lwin")
def Lwin():
    return "Hello Lwin Me Me Khaing"
