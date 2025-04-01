from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "HLC Colour Picker Backend"
if __name__ == '__main__':
    app.run()
