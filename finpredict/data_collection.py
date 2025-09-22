from finviz.screener import Screener
from finviz import * 
import pandas as pd
import json
import requests
from finpredict.config import get_config_str


def get_data():
    token = get_config_str("token", "", "Token for Tiingo API")


    filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
    # Get the first 50 results sorted by price ascending
    stock_list = Screener(filters=filters, order='price', rows=10000)

    # Export the screener results to .csv
    screener_result_path = get_config_str("screener_result_path", "data/tickers.csv", "Path to save screener results")

    stock_list.to_csv(filename=screener_result_path)

    data_dir = get_config_str("data_dir", "data", "Directory to save stock data")

    for stock in stock_list:  # Loop through 10th - 20th stocks
        print(stock['Ticker'], stock['Price']) # Print symbol and price
        s = get_stock(stock["Ticker"])
        with open(f"{data_dir}/{stock['Ticker']}.json", "w") as f:
            f.write(json.dumps(s))
        with open(f"{data_dir}/{stock['Ticker']}.csv", "w") as f:
            f.write(requests.get(f"https://api.tiingo.com/tiingo/daily/{stock['Ticker']}/prices?startDate=2012-1-1&endDate=2019-6-1&token={token}&format=csv").text)
        with open(f"{data_dir}/news/{stock['Ticker']}.json", "w") as f:
            f.write(requests.get(f"https://api.tiingo.com/tiingo/news?tickers={stock['Ticker']}&startDate=2012-1-1&endDate=2019-6-1&token={token}").text)
