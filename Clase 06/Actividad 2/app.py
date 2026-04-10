from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, mi primera app con Cambios Reales!"