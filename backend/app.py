
import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/match')
def match_colors():
    return jsonify({"status": "success", "match": "dummy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
