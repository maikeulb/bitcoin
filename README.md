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
