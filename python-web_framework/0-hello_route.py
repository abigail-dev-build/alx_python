from flask import Flask

app = Flask(__name__)

"""
this function displays string "Hello HBNB!" on the path "/".
"""
@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    