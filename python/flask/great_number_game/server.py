import random
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def index():
    random_number = random.randint(1, 100)
    session['random_number'] = random_number
    return render_template("index.html")


@app.route("/guess", methods=['POST'])
def guess():
    guess_number = int(request.form['number'])
    return render_template("guess.html", guess_number=guess_number, random_number=session['random_number'])


if __name__ == "__main__":
    app.run(debug=True)
