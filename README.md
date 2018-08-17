# Bitcoin API client
API client that consumes bitcoin data from bitmex API endpoint:

https://www.bitmex.com/api/v1/instrument/compositeIndex?symbol=.XBT&filter=%7B%22timestamp.time%22%3A%2210%3A55%3A00%22%2C%22reference%22%3A%22BSTP%22%7D&count=100&reverse=true

Outputting JSON to an endpoint with these values:

```
[

    {

        "{date}”,

        “price”:”{value}”,

        "priceChange": "{up/down/same}",

        "change": "{amount}",

        "dayOfWeek":"{name}”,

        "highSinceStart": "{true/false}”,

        “lowSinceStart": "{true/false}”

    }

]
```

Results ordered by oldest date first:

 
- "Price change" is since previous day in the list, first day can be “na”

- "change" is the difference between previous day in list. “na” for first

- "day of week" is name of the day (Saturday, Tuesday, etc)

- "high since start” / “low since start” is if this is the highest/lowest price since the oldest date in the list.

Sample Usage
---------------
`http localhost:5000/api/bitcoins`

```
[
    {
        "change": "na",
        "day": 1,
        "dayOfWeek": "Thursday",
        "highSinceStart": true,
        "lowSinceStart": true,
        "price": 6470.01,
        "priceChange": "na"
    },
...
    {
        "change": -211.64,
        "day": 100,
        "dayOfWeek": "Wednesday",
        "highSinceStart": false,
        "lowSinceStart": false,
        "price": 9156.16,
        "priceChange": "down"
    }
]
```


Run
---
With docker:
```
docker-compose build
docker-compose up
Go to http://localhost:5000 and visit one of the above endpoints
```

Alternatively, set the `FLASK_APP` env variable
to bitcoin_challenge.py, and install the python dependencies (e.g. `pip install
-r requirements.txt`)


`cd` into `./bitcoin_challenge` (if you are not already); then run:
```
flask run
Go to http://localhost:5000 and visit api/bitcoins
```
