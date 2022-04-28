from flask import Flask, redirect, url_for, render_template, request
from main import *

app = Flask(__name__)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        data = ("tandinhd@icloud.com", "hong@gmail.com", "How are you?")
        main(data)
        return redirect(url_for("user", name=user))

    else:
        return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/")
def start():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
    