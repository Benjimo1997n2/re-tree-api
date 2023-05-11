from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATABASE_FILE = "users.json"

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our re-tree-api!</h1>"

def load_users():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}
    return users


def save_users(users):
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f, indent=4)


@app.route("/create_user", methods=["POST"])
def create_user():
    users = load_users()
    username = request.form["username"]
    if username in users:
        return jsonify({"status": "error", "message": "User already exists"}), 400

    users[username] = {
        "CO2": int(request.form["CO2"]),
        "CO2_per_sec": int(request.form["CO2_per_sec"]),
        "trees": json.loads(request.form["trees"]),
    }
    save_users(users)
    return jsonify({"status": "success", "message": "User created"}), 201


@app.route("/save_data", methods=["POST"])
def save_data():
    users = load_users()
    username = request.form["username"]

    if username not in users:
        return jsonify({"status": "error", "message": "User not found"}), 404

    users[username]["trees"] = json.loads(request.form["trees"])
    users[username]["CO2"] = int(request.form["CO2"])
    users[username]["CO2_per_sec"] = int(request.form["CO2_per_sec"])
    save_users(users)
    return jsonify({"status": "success", "message": "User data saved"}), 200


@app.route("/visit_user/<string:username>", methods=["GET"])
def visit_user(username):
    users = load_users()

    if username not in users:
        return jsonify({"status": "error", "message": "User not found"}), 404

    return jsonify(users[username]), 200

@app.route("/all_users", methods=["GET"])
def all_users():
    users = load_users()
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True)
