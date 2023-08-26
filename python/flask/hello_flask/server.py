
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/lists')
def render_lists():
    student_info = [
        'name'
    ]


@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)


# @app.route('/dojo')
# def success():
#     return "Dojo!"


# @app.route('/hello/<string:banana>/<int:num>')
# def hello(banana, num):
#   n


# @app.route('/repeat/<int:num>/<string:banana>')
# def repeat(num, banana):
#     return '{}<br>'.format(banana) * num


if __name__ == "__main__":
    app.run(debug=True)
