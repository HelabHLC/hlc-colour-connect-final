from flask import Flask, send_from_directory, jsonify, request
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '../frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR)

@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route('/api/match')
def match_colors():
    return jsonify({"status": "success", "match": "dummy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
