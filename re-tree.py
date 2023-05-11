from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import firebase_admin
from firebase_admin import credentials, db
import os

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("re-tree-api-firebase-adminsdk-qjv99-1e27f18d10.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://re-tree-api-default-rtdb.europe-west1.firebasedatabase.app/'
})

@app.route('/save_data', methods=['POST'])
def save_data():
    username = request.form.get('username')
    trees = request.form.get('trees')
    CO2 = request.form.get('CO2')
    CO2_per_sec = request.form.get('CO2_per_sec')

    # Save data to Firebase
    data = {
        "username": username,
        "trees": trees,
        "CO2": CO2,
        "CO2_per_sec": CO2_per_sec
    }

    ref = db.reference('users')
    ref.child(username).set(data)

    return jsonify({"message": "Data saved successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
