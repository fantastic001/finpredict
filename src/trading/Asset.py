from typing import *
class Asset(object):
    def __init__(self, ticker: str, count: int):
        
        self.ticker = ticker
        
        self.count = count
        
    
    def get_total_value(self, source: Source) -> float:
        pass
      