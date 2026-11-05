from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Read API key from environment variable
API_KEY = os.environ.get("API_KEY")


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my Python Flask API!",
        "status": "Working"
    })


@app.route("/students")
def students():
    return jsonify({
        "students": [
            {"id": 1, "name": "Arbaz", "department": "BSCS"},
            {"id": 2, "name": "Ahmed", "department": "BSCS"},
            {"id": 3, "name": "Ali", "department": "BSCS"}
        ]
    })


@app.route("/secret")
def secret():
    user_key = request.headers.get("X-API-Key")

    if not API_KEY or user_key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    return jsonify({
        "message": "Access granted!",
        "data": "This is protected information."
    })


if __name__ == "__main__":
    app.run(debug=True)