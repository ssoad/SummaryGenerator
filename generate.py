#!/usr/bin/env python3
"""
this module creates the server and provides the text
"""
from flask import Flask, request, render_template
from process import processText

app = Flask(__name__)


@app.route('/')
def form():
    return render_template("form.html")


@app.route('/', methods=['POST'])
def getText():
    text = request.form['textInput']
    text = processText(text)
    return (f"<h1>Result</h1> <p>{text}</p>")


if __name__ == "__main__":
    app.run(debug=True)
