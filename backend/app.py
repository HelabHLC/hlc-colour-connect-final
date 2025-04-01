import os
import json
from flask import Flask, send_from_directory, jsonify, request
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976
import csv

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '../frontend')
CSV_PATH = os.path.join(BASE_DIR, '../data/HLC-Colour-Atlas-XL_ColourValues_v1_03302025.csv')

def hex_to_lab(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    rgb = sRGBColor(r/255.0, g/255.0, b/255.0)
    lab = convert_color(rgb, LabColor)
    return [lab.lab_l, lab.lab_a, lab.lab_b]

# CSV-Daten laden
hlc_colors = []
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            name = row["Name"]
            hex_val = row["Hex"]
            lab = hex_to_lab(hex_val)
            hlc_colors.append({"name": name, "hex": hex_val.upper(), "lab": lab})
        except Exception:
            continue

def delta_e(lab1, lab2):
    return sum((a - b) ** 2 for a, b in zip(lab1, lab2)) ** 0.5

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route("/api/match")
def match_color():
    hex_input = request.args.get("hex", "").lstrip("#")
    if len(hex_input) != 6:
        return jsonify({"error": "Invalid HEX"}), 400
    try:
        input_lab = hex_to_lab(hex_input)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    best_match = None
    min_delta = float("inf")
    for color in hlc_colors:
        dE = delta_e(input_lab, color["lab"])
        if dE < min_delta:
            min_delta = dE
            best_match = color

    return jsonify({
        "input": "#" + hex_input.upper(),
        "match": best_match,
        "deltaE": round(min_delta, 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
