from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello World"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/")
def start():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()