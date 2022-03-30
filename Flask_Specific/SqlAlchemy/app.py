from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name=None):
    # return f"Hello, {escape(name)}!"
    return render_template('hello.html', name=name)

if __name__== "__main__":
    app.run(debug=True)
    # app.run(debug=True,port=8000)