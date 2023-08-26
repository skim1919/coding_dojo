# don't forget to import redirect!
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "hello"

# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
    else:
        return redirect(url_for("login"))
    return f"<h1>{user}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
