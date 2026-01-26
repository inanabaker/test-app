import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World hilser fra Argo!"

def get_secret():
    return os.getenv("InanaTopSecretKey", "SECRET NOT FOUND")

@app.route("/")
def index():
    return render_template(
        "index.html",
    )

@app.route("/reveal")
def show_secret():
    secret = get_secret()
    return render_template(
        "secret.html", secret=secret
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)