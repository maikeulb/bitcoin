import sys
import requests
import json
from datetime import datetime
from flask import jsonify, current_app, request
from app.api import api

max_price = -sys.maxsize - 1
min_price = sys.maxsize


@api.route('/bitcoins')
def get_bitcoin_data():

    url = current_app.config['API_URL']

    data = requests.get(url).json()

    date_string_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    bitcoins = []

    for i in range(1, 100):
        info = {
            'day': i,
            'price': data[i]["lastPrice"],
            'change': "na" if i == 1 else round(data[i]["lastPrice"] - data[i - 1]["lastPrice"], 2),
            'priceChange': "na" if i == 1 else price_change(data[i - 1]["lastPrice"],
                                                            data[i]["lastPrice"]),
            'dayOfWeek': datetime.strptime(data[i]["timestamp"],
                                           date_string_format).strftime('%A'),
            'highSinceStart': is_high_since_start(data[i]["lastPrice"]),
            'lowSinceStart': is_low_since_start(data[i]["lastPrice"])
        }
        bitcoins.append(info)
    return jsonify(bitcoins), 200


def price_change(prev, curr):
    if curr > prev:
        priceChange = "up"
    elif curr < prev:
        priceChange = "down"
    else:
        priceChange = "same"
    return priceChange


def is_high_since_start(price):
    global max_price
    if price > max_price:
        max_price = price
        return True
    return False


def is_low_since_start(price):
    global min_price
    if price < min_price:
        min_price = price
        return True
    return False
