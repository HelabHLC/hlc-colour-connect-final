# Flask app goes here
from flask import Flask, send_from_directory
import os

# Verzeichnis-Konfiguration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '../frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')

# Startseite: index.html
@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

# Alle anderen statischen Dateien (CSS, JS, PNG, ...)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

# App starten
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
