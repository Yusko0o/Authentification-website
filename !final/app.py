from flask import Flask, render_template
from routes.login import auth
import sqlite3
from routes.sign import sign

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(sign)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signin")
def sign_in_page():
    return render_template("signin.html")

if __name__ == "__main__":
    app.run(debug=True)