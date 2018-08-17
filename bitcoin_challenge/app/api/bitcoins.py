import requests
import json
from datetime import datetime
from flask import jsonify, current_app, request
from app.api import api


@api.route('/bitcoins')
def get_bitcoin_data():

    url = current_app.config['API_URL']

    data = requests.get(url).json()

    date_string_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    bitcoins = {
        'Day': 1,
        'price': data[1]["lastPrice"],
        'priceChange': "up",
        'dayOfWeek': datetime.strptime(data[1]["timestamp"],
                                       date_string_format).strftime('%A'),
        'highSinceStart': "true",
        'lowSinceStart': "true",
    }

    return jsonify(bitcoins), 200
