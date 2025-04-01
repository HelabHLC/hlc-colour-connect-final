
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="../frontend")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/match_rgb")
def match_rgb():
    rgb = request.args.get("rgb", "255,255,255")
    # Dummy-Matching-Rückgabe
    return jsonify({
        "name": "Sample Colour",
        "hex": "#FFFFFF",
        "lab": "100, 0, 0"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
