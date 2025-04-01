
from flask import Flask, request, jsonify
import csv
import os
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976

app = Flask(__name__)

# CSV-Pfad (HLC-Datenbank)
CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/HLC-Colour-Atlas-XL_ColourValues_v1_03302025.csv")

# CSV einlesen und in Liste umwandeln
def load_hlc_data():
    colors = []
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                lab = [float(row['L']), float(row['A']), float(row['B'])]
                colors.append({
                    "name": row["Name"],
                    "hex": row["sRGB-hex"],
                    "lab": lab
                })
            except:
                continue
    return colors

hlc_colors = load_hlc_data()

# HEX zu LAB
def hex_to_lab(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    srgb = sRGBColor(r / 255.0, g / 255.0, b / 255.0)
    lab = convert_color(srgb, LabColor)
    return [lab.lab_l, lab.lab_a, lab.lab_b]

@app.route("/api/match")
def match_color():
    hex_input = request.args.get("hex", "").strip("#")
    if len(hex_input) != 6:
        return jsonify({"error": "Ungültiger HEX-Wert"}), 400

    try:
        input_lab = hex_to_lab(hex_input)
    except:
        return jsonify({"error": "Fehler bei Umrechnung"}), 400

    best_match = None
    min_delta = float("inf")
    for color in hlc_colors:
        dE = delta_e_cie1976(LabColor(*input_lab), LabColor(*color["lab"]))
        if dE < min_delta:
            min_delta = dE
            best_match = color

    return jsonify({
        "input": "#" + hex_input.upper(),
        "match": {
            "name": best_match["name"],
            "hex": best_match["hex"],
            "lab": best_match["lab"],
            "deltaE": round(min_delta, 2)
        }
    })

@app.route("/")
def index():
    return "🎯 HLC Colour Match API läuft."

if __name__ == "__main__":
    app.run(debug=True)
