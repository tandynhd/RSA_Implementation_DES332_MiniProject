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
        if username == "":
            username = "tester"  # Email account of sender
        if sEmail == "":
            sEmail = "ktp.des332work@gmail.com"  # Email account of sender
        if spassword == "":
            spassword = "ktp.1234"
        if rEmail == "":
            rEmail = "hackdorji@gmail.com"  # Email account of receiver
            # rEmail = "hung.nd.siit@gmail.com"  # Email account of receiver
        if message == "":
            message = "Hello! This is KTP, send an email securely using our services."

        data = [username, sEmail, spassword, rEmail, message]
        main(data)
        # return f"Hello {data}!"
        return render_template("result.html", value = data)

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
    