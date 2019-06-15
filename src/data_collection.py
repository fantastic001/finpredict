from finviz.screener import Screener
from finviz import * 
import pandas as pd
import json
import requests

config = {}
with open("config.json") as f:
    config = json.loads(f.read())
token = config["token"]


filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
# Get the first 50 results sorted by price ascending
stock_list = Screener(filters=filters, order='price', rows=10000)

# Export the screener results to .csv
stock_list.to_csv(filename="data/tickers.csv")

for stock in stock_list:  # Loop through 10th - 20th stocks
    print(stock['Ticker'], stock['Price']) # Print symbol and price
    s = get_stock(stock["Ticker"])
    with open("data/%s.json" % stock["Ticker"], "w") as f:
        f.write(json.dumps(s))
    with open("data/%s.csv" % stock["Ticker"], "w") as f:
        f.write(requests.get("https://api.tiingo.com/tiingo/daily/%s/prices?startDate=2012-1-1&endDate=2019-6-1&token=%s&format=csv" % (stock["Ticker"], token)).text)
    with open("data/news/%s.json" % stock["Ticker"], "w") as f:
        f.write(requests.get("https://api.tiingo.com/tiingo/news?tickers=%s&startDate=2012-1-1&endDate=2019-6-1&token=%s" % (stock["Ticker"], token)).text)
