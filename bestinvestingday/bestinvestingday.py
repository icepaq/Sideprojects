import requests
from datetime import datetime


api_key = 'XZG7KAERH7D8GWOE'

# Calling AlphaVantage API
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&'
                        'symbol=SPY&outputsize=full&apikey=' + api_key)

# Filtering out meta data
prices = response.json()['Time Series (Daily)']

counter = 0  # Being used to made sure only about 2 years of data is stored
dates = []  # Will store every single date that is returned with the API

# Will store each day from dates as the key and the value will be the day of the week
date_day = {
    '0000-00-00': 'null',
}

days = []

# Appending all dates from the last 2 years
for i in prices:
    if counter > 500:
        break

    counter += 1
    dates.append(i)

# Refer to line 14. Appending each date.
for i in dates:
    date_day[i] = datetime.fromisoformat(i).weekday()

average_prices = {}  # Will store each day of the week and the average price

for a in range(5):
    count = 0
    cost = 0.00

    for b in date_day:

        # Making sure that we are only processing information for the specific day
        if date_day[b] != a:
            continue

        cost = cost + float(prices[b]['1. open'])
        count += 1

    if cost == 0 or count == 0:
        average_prices[a] = 0
    else:
        average_prices[a] = cost / count


print(average_prices)
