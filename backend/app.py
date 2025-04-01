import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/match')
def match_colors():
    hex_code = request.args.get("hex", "#ffffff")
    best_match = {"name": "H315_L095_C005", "hex": "#F6EEF8"}
    return jsonify({"status": "success", "input": hex_code, "match": best_match})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
