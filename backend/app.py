
import os
import json
import csv
from flask import Flask, request, jsonify, send_from_directory
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

app = Flask(__name__, static_folder='../frontend', static_url_path='')

def hex_to_lab(hex_code):
    hex_code = hex_code.strip().lstrip("#")
    rgb = sRGBColor(*(int(hex_code[i:i+2], 16) / 255.0 for i in (0, 2 ,4)))
    lab = convert_color(rgb, LabColor)
    return lab

def load_hlc_data():
    hlc_data = []
    with open("data/HLC-Colour-Atlas-XL_ColourValues_v1_03302025.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lab = LabColor(float(row["L"]), float(row["A"]), float(row["B"]))
            hlc_data.append({
                "name": row["Name"],
                "hex": row["HEX"],
                "lab": lab
            })
    return hlc_data

hlc_database = load_hlc_data()

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api/match")
def match():
    hex_code = request.args.get("color", "")
    threshold = float(request.args.get("delta", 5.0))
    input_lab = hex_to_lab(hex_code)
    
    closest = None
    closest_distance = float("inf")
    for entry in hlc_database:
        dist = delta_e_cie2000(input_lab, entry["lab"])
        if dist < closest_distance:
            closest = entry
            closest_distance = dist

    return jsonify({
        "input": hex_code,
        "match": closest["hex"] if closest else None,
        "name": closest["name"] if closest else "Unknown",
        "deltaE": round(closest_distance, 3)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
