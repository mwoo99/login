from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def login():
    return render_template("loginTemp.html")

@app.route("/authentication/", methods = ["POST"])
def authentication():
    if request.form["user"]=="user" and request.form["pass"]=="pass":
        return render_template("authentication.html", status = "success")
    else:
        return render_template("authentication.html", status = "failure")

if __name__ == "__main__":
    app.debug = True
    app.run()
 
