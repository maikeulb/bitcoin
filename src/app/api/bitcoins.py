import sys
import requests
from datetime import datetime
from flask import g, jsonify, current_app
from app.api import api


@api.before_app_request
def before_request():
    g.max_price = -sys.maxsize - 1
    g.min_price = sys.maxsize


@api.route('/bitcoins')
def get_bitcoin_data():

    url = current_app.config['API_URL']

    data = requests.get(url).json()
    date_string_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    bitcoins = []

    # for i in range(0, 100):
    for i in range(100, -1, -1):
        info = {
            'day': i + 1,
            'price': data[i]["lastPrice"],
            'change': "na" if i == 0 else round(data[i]["lastPrice"] - data[i - 1]["lastPrice"], 2),
            'priceChange': "na" if i == 0 else price_change(data[i - 1]["lastPrice"], data[i]["lastPrice"]),
            'dayOfWeek': datetime.strptime(data[i]["timestamp"], date_string_format).strftime('%A'),
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
    if price > g.max_price:
        g.max_price = price
        return True
    return False


def is_low_since_start(price):
    if price < g.min_price:
        g.min_price = price
        return True
    return False
