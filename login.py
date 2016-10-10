from flask import Flask, render_template, request, url_for, session, redirect
import hashlib
import csv

passFile = "data/passLog.csv"

app = Flask(__name__)
app.secret_key = '<j\x9ch\x80+\x0b\xd2\xb6\n\xf7\x9dj\xb8\x0fmrO\xce\xcd\x19\xd49\xe5S\x1f^\x8d\xb8"\x89Z'

def register(username, password):
    passFileReader = csv.reader(open(passFile))
    for i in passFileReader:
        if username == i[0]:
            return "You are already registered."
    with open(passFile, "a") as f:
        w = csv.writer(f)
        w.writerow([username, hashlib.sha1(password).hexdigest()])
    return "You are now successfully registered."

def checkLogin(username,password):
    passFileReader = csv.reader(open(passFile))
    for i in passFileReader:
        if username == i[0]:
            if i[1] == hashlib.sha1(password).hexdigest():
                return "You are logged in."
            return "Incorrect password!"
    return "No such username"


@app.route("/")
@app.route("/login/")
def login():
    if "user" in session:
        return render_template("loggedIn.html", status = "You are logged in.")
    return render_template("loginTemp.html")

@app.route("/authentication/", methods = ["GET", "POST"])
def authentication():
    if request.form["enter"] == "Register":
        register_message = register(request.form["user"],request.form["pass"])
        return render_template("authentication.html", status = register_message)
    if request.form["enter"] == "Login":
        session["user"] = request.form["user"]
        login_message = checkLogin(request.form["user"],request.form["pass"])
        return render_template("loggedIn.html", status = login_message)

@app.route("/logout/")    
def logout():
    session.pop("user")
    return redirect(url_for("login"))
        
if __name__ == "__main__":
    app.debug = True
    app.run()
