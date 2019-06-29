from typing import *
class Source(object):
    def __init__(self, file_path: str):
        self.time = 0
        self.file_path = file_path
        
    def get_time(self):
        return self.time

    def forward(self, dt=1):
        self.time += dt

    def get_close(self, ticker: str, dt: int) -> float:
        pass
    
    def get_open(self, ticker: str, dt: int) -> float:
        pass
    
    def get_low(self, ticker: str, dt: int) -> float:
        pass
    
    def get_high(self, ticker: str, dt: int) -> float:
        pass
    
    def get_volume(self, ticker: str, dt: int) -> float:
        pass
      
    def get_tickers(self):
        return [
            "AAPL",
            "GOGL",
            "MSFT"
        ]
