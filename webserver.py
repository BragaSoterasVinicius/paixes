import json
from crypt import methods

import aquarium
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/createfish', methods=['POST'])
def create_fish():
    record = json.loads(request.data)
    energy = int(record['energy'])
    appearance = str(record['appearance'])
    x = int(record['x'])
    y = int(record['y'])
    aquarium.create_fish(appearance, energy, x, y)
    return jsonify({'success': True})

@app.route('/give_food', methods=['POST'])
def give_food():
    record = json.loads(request.data)
    x = int(record['x'])
    y = int(record['y'])
    aquarium.jogar_racao(x, y)
    return jsonify({'success': True})


@app.route('/getaquarium', methods=['GET'])
def get_aquarium():
    return aquarium.get_aquarium()

