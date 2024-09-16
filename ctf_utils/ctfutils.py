from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cryptography")
def crypto_homepage():
    return render_template("crypto.html")


@app.route("/")
def homepage():
    return render_template("homepage.html")
