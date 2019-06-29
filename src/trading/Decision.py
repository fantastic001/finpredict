from typing import *
class Decision(object):
    
    BUY = 0
    SELL = 1
    
    def __init__(self, action: int, ticker: str, count: int):
        
        self.action = action
        
        self.ticker = ticker
        
        self.count = count
        
    
    def buy(ticker: str, count: int) -> Decision:
        return Decision(self.BUY, ticker, count)
    
    def sell(ticker: str, count: int) -> Decision:
        return Decision(self.SELL, ticker, count)
      
