# import mimetypes
# from turtle import pd
from flask import Flask, Response
from flask_cors import CORS
import os
import pandas as pd

app = Flask(__name__)

CORS(app)

# Statt Pfad mit Schrägstrich, oder Rückschlag anzugeben, os.path.join nutzen, da es sonst von
# einigen Betriebssystemen falsch interperetiert
training_data = pd.read_csv(os.path.join('data', 'auto-mpg.csv'))


@app.route("/", methods=["GET"])
def index():
    return{"Hallo": "Erde", "Hi": "Mars", "Ähäoü": "Venus"}


@app.route("/hallo_welt", methods=["GET"])
def hello_world():
    return "<p>Hallo Welt!</p>"


@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype='application/json')
