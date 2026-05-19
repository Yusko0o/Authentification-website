from flask import Blueprint, render_template, request
import sqlite3

auth = Blueprint("auth", __name__)

@auth.route("/log_in", methods=["GET"])
def login_page():
    return render_template("index.html")

@auth.route("/log_in", methods=["POST"])
def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        connect = sqlite3.connect("users.db")
        cursor= connect.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()
        connect.close()

        if not user:
            return "No account"

        if user[0] == password:
            return "You're logged in !"
        else:
            return "Incorrect !"
    except Exception as e:
        return f"Error: {e}"