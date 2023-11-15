from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    return


@app.route("/login", methods=["POST"])
def login():
    return


if __name__ == "__main__":
    app.run(debug=True)
