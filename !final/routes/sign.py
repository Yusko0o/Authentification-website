from flask import Blueprint, request
import sqlite3

sign = Blueprint("sign", __name__)

@sign.route("/sign_in", methods=["POST"])
def sign_in():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        connect = sqlite3.connect("users.db")
        cursor= connect.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing = cursor.fetchone()

        if existing:
            return "Email already exisits"

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, password)
        )

        connect.commit()
        connect.close()

        return "User created ! You can now log in !"
    
    except Exception as e:
        return f"Error : {e}"