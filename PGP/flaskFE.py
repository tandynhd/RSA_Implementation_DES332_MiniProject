from flask import Flask, redirect, url_for, render_template, request
from main import main

app = Flask(__name__)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        sEmail = request.form["semail"]
        spassword = request.form["spassword"]
        rEmail = request.form["remail"]
        message = request.form["email"]
        if sEmail == "":
            sEmail = "ktp.des332work@gmail.com"  # Email account of sender
        if spassword == "":
            spassword = "ktp.1234"
        if rEmail == "":
            rEmail = "hackdorji@gmail.com"  # Email account of sender
        data = [username, sEmail, spassword, rEmail, message]
        main(data)
        # return f"Hello {data}!"
        return render_template("result.html", info = data)

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
    