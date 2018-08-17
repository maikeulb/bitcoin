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
    bitcoin1 = {
        'day': 1,
        'price': data[1]["lastPrice"],
        'change': "na" if 1 == 1 else round(data[2]["lastPrice"] - data[1]["lastPrice"], 2),
        'priceChange': "na" if 1 == 1 else price_change(data[1]["lastPrice"],
                                                        data[2]["lastPrice"]),
        'dayOfWeek': datetime.strptime(data[1]["timestamp"],
                                       date_string_format).strftime('%A'),
        'highSinceStart': is_high_since_start(data[1]["lastPrice"]),
        'lowSinceStart': is_low_since_start(data[1]["lastPrice"])
    }
    print(max_price)
    print(min_price)
    bitcoin2 = {
        'day': 2,
        'price': data[2]["lastPrice"],
        'priceChange': "na" if 2 == 1 else price_change(data[1]["lastPrice"],
                                                        data[2]["lastPrice"]),
        'change': "na" if 2 == 1 else round(data[2]["lastPrice"] - data[1]["lastPrice"], 2),
        'dayOfWeek': datetime.strptime(data[2]["timestamp"],
                                       date_string_format).strftime('%A'),
        'highSinceStart': is_high_since_start(data[2]["lastPrice"]),
        'lowSinceStart': is_low_since_start(data[2]["lastPrice"])
    }
    bitcoins = [bitcoin1, bitcoin2]

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
