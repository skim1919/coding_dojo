from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def submitted_my_survey():
    # print(request.form)  # immutable dictionary object
    # session['name'] = request.form['name']
    # session['language'] = request.form['language']
    # session['location'] = request.form['location']
    # session['comment'] = request.form['comment']
    # return render_template("results.html")

    return render_template("results.html", name=request.form["name"], language=request.form["language"], location=request.form["location"], comment=request.form["comment"])


if __name__ == "__main__":
    app.run(debug=True)
