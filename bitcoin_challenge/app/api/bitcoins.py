import requests
import json
from flask import jsonify, current_app, request
from app.api import api


@api.route('/bitcoins')
def get_bitcoin_data():

    url = current_app.config['API_URL']

    data = requests.get(url).json()
    return jsonify(data), 200
