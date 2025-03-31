from flask import Flask, send_from_directory
import os

# Absoluter Pfad zur frontend/index.html ermitteln
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '../frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Optional: Alle statischen Dateien wie JS, CSS, etc.
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
