
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Dummy-Daten simulieren Farbabgleich
with open("backend/dummy_colors.json", "r") as f:
    color_db = json.load(f)

@app.route("/api/match")
def match_colors():
    hex_colors = request.args.get("colors", "").split(",")
    delta = float(request.args.get("delta", 5.0))
    result = []

    for hex_code in hex_colors:
        # Mock: immer denselben Satz zurückgeben
        result.extend(color_db)

    return jsonify(result)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # <- Das hier ist wichtig!
    app.run(host='0.0.0.0', port=port)

