from flask import Flask, send_from_directory, request, jsonify
import os
import csv

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# Load HLC Data (Name, HEX, L, A, B)
hlc_colors = []
csv_path = os.path.join(os.path.dirname(__file__), '../data/HLC-Colour-Atlas.csv')
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        hlc_colors.append({
            "name": row["Name"],
            "hex": row["HEX"],
            "lab": (float(row["LAB_L"]), float(row["LAB_A"]), float(row["LAB_B"]))
        })

def delta_e(lab1, lab2):
    return sum((a - b) ** 2 for a, b in zip(lab1, lab2)) ** 0.5

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/match', methods=['GET'])
def match_color():
    try:
        l = float(request.args.get('L'))
        a = float(request.args.get('A'))
        b = float(request.args.get('B'))
        threshold = float(request.args.get('delta', 5.0))

        closest = min(hlc_colors, key=lambda c: delta_e((l, a, b), c["lab"]))
        diff = delta_e((l, a, b), closest["lab"])
        if diff <= threshold:
            return jsonify({
                "match": closest,
                "deltaE": round(diff, 2)
            })
        else:
            return jsonify({"match": None, "deltaE": round(diff, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
