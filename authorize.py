import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3

load_dotenv()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')
jwt = JWTManager(app)

# creating database file
connect = sqlite3.connect(os.getenv('DATABASE_URL'))
cursor = connect.cursor()

# creating users table
cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS users 
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )'''
)

connect.commit()
connect.close

#api endpoint for home
@app.route("/")
def home():
    return

# api endpoint for registering users
@app.route("/register", methods=["POST"])
def register():
    return


# api endpoint for logging users in
@app.route("/login", methods=["POST"])
def login():
    return


if __name__ == "__main__":
    app.run(debug=True)