
from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='../frontend')
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/hlc_rgb_reference.json')

# Farben laden
with open(DATA_PATH, 'r') as f:
    COLORS = json.load(f)

def rgb_distance(c1, c2):
    return sum((c1[i] - c2[i]) ** 2 for i in range(3)) ** 0.5

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/match_rgb')
def match_rgb():
    rgb_param = request.args.get("rgb", "")
    try:
        r, g, b = map(int, rgb_param.split(","))
        input_rgb = [r, g, b]
    except:
        return jsonify({"error": "Invalid RGB"}), 400

    best = min(COLORS, key=lambda c: rgb_distance(input_rgb, [c["R"], c["G"], c["B"]]))
    return jsonify({
        "name": best["Name"],
        "hex": best["Hex"],
        "rgb": [best["R"], best["G"], best["B"]]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    