import os
from flask import Flask, render_template, jsonify
from sqlalchemy import text

from databaseconnection import engine

app = Flask(__name__)

init_sql = "init.sql"

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

def init_db():
    with engine.begin() as conn:  # begin() = auto commit
        with open("init.sql", "r") as f:
            sql_script = f.read()
        conn.exec_driver_sql(sql_script)
    print("Database initialisert!")

@app.route("/test-data")
def get_test_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, text, ST_AsText(geom) FROM inanas_data;"))
        rows = result.fetchall()

        data = [
            {"id": row[0], "text": row[1], "geom": row[2]}
            for row in rows
        ]
    return jsonify(data)

print("Init DB...")
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)