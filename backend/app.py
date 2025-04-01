
from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

basedir = os.path.dirname(__file__)
json_path = os.path.join(basedir, "dummy_colors.json")

with open(json_path, "r") as f:
    color_db = json.load(f)

@app.route("/api/match")
def match_colors():
    hex_colors = request.args.get("colors", "").split(",")
    delta = float(request.args.get("delta", 5.0))
    result = []

    for hex_code in hex_colors:
        result.extend(color_db)

    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
