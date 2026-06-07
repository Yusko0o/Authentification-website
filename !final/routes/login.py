from flask import Blueprint, render_template, request
import sqlite3
import hashlib as h
import os

auth = Blueprint("auth", __name__)

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "users.db")

@auth.route("/log_in", methods=["GET"])
def login_page():
    return render_template("index.html")

@auth.route("/log_in", methods=["POST"])
def login():
    try:
        email = request.form.get("email") # email request
        password = request.form.get("password") # password request

        hashPassword = h.sha1(password.encode()).hexdigest() # password getting hashed

        connect = sqlite3.connect(DB_PATH) # connecting to the database
        cursor= connect.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE email = ?", # selecting the labels in the database
            (email,)
        )

        user = cursor.fetchone()
        connect.close()

        if not user:
            return "No account"

        if user[0] == hashPassword: # hashed password getting compared with other hashed password
            return "You're logged in !"
        else:
            return "Incorrect !"
    except Exception as e:
        return f"Error: {e}"
