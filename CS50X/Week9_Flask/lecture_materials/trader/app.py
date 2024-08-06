from flask import Flask
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def method_name():
    render_template("index.html")
