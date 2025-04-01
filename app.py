
from flask import Flask, send_from_directory, jsonify, request
import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '../frontend')
ICC_DIR = os.path.join(BASE_DIR, '../icc')
CSV_PATH = os.path.join(BASE_DIR, '../data/HLC-Colour-Atlas-XL_ColourValues_v1.csv')

app = Flask(__name__, static_folder=FRONTEND_DIR)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/icc-profiles')
def list_icc_profiles():
    files = os.listdir(ICC_DIR)
    profiles = [f.replace('.icc', '') for f in files if f.endswith('.icc')]
    return jsonify(sorted(profiles))

@app.route('/api/colors')
def filter_colors():
    icc = request.args.get('icc')
    filtered_colors = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cmyk_value = row.get(f"CMYK_{icc}", "").strip()
                if cmyk_value:
                    filtered_colors.append({
                        "name": row.get("Name"),
                        "hex": row.get("HEX"),
                        "lab": [row.get("L"), row.get("A"), row.get("B")]
                    })
    return jsonify(filtered_colors)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
