from typing import *
import os 
import pandas as pd
import datetime
class Source(object):
    def __init__(self, file_path: str):
        self.time = 0
        self.file_path = file_path
        self.tickers = {}
        tickers = self.get_tickers()
        for ticker in tickers:
            self.tickers[ticker] = pd.read_csv("%s/%s.csv" % (self.file_path, ticker)).set_index("date").reindex(pd.date_range('2014', freq='D', periods=3300-2*365).map(lambda x: datetime.datetime.strftime(x, "%Y-%m-%d"))).fillna(method="ffill").fillna(method="bfill")
    def get_time(self):
        return self.time

    def get_ticker(self, ticker, column, dt=0):
        try:
            return self.tickers[ticker][column][self.time + dt]
        except KeyError:
            return 0

    def forward(self, dt=1):
        self.time += dt

    def get_close(self, ticker: str, dt: int) -> float:
        return self.get_ticker(ticker, "adjClose", dt)
    
    def get_open(self, ticker: str, dt: int) -> float:
        return self.get_ticker(ticker, "adjOpen", dt)
    
    def get_low(self, ticker: str, dt: int) -> float:
        return self.get_ticker(ticker, "adjLow", dt)
    
    def get_high(self, ticker: str, dt: int) -> float:
        return self.get_ticker(ticker, "adjHigh", dt)
    
    def get_volume(self, ticker: str, dt: int) -> float:
        return self.get_ticker(ticker, "adjVolume", dt)
    
    def get_dividend(self, ticker: str, dt: int) -> float:
        return self.get_ticker(ticker, "divCash", dt)
      
    def get_tickers(self):
        return list(f.split(".")[0] for f in os.listdir(self.file_path) if f.endswith(".csv"))
