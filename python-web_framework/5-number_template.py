"""
Basic Flask Web Server
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


"""
this function displays string "Hello HBNB!" on the path "/".
"""
@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

"""
this function displays string "HBNB" on the path "/hbnb".
"""
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

"""
this function displays the text a user adds to the path.
It replaces any '_' to empty space(' ')
"""
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"

"""
this function displays a default text "is cool" when the path /python is enter and the user does not specify a text.
It replaces any '_' to empty space(' ')
"""
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"

"""
this function displays “n is a number” only if n is an integer and "page not found" if it is a string
"""
@app.route("/number/<int:n>", strict_slashes=False)
def check_if_number(n):
 return f"{n} is a number"


"""
this function displays a HTML page only if n is an integer
"""
@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html_if_number(n):
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
    