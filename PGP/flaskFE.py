from flask import Flask, redirect, url_for, render_template, request
from main import main

app = Flask(__name__)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        sEmail = request.form["semail"]
        rEmail = request.form["remail"]
        message = request.form["email"]
        data = [username, sEmail, rEmail, message]
        main(data)
        return f"Hello {data}!"

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
    