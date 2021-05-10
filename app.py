from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Hello<h1> This is my linear regression project!'


if __name__ == "__main__":
    app.run(debug=True)