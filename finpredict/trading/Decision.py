from typing import *
class Decision(object):
    
    BUY = 0
    SELL = 1
    
    def __init__(self, action: int, ticker: str, count: int):
        
        self.action = action
        
        self.ticker = ticker
        
        self.count = count
        
    
    @staticmethod
    def buy(ticker: str, count: int):
        return Decision(Decision.BUY, ticker, count)
    
    @staticmethod
    def sell(ticker: str, count: int):
        return Decision(Decision.SELL, ticker, count)
    
    def __str__(self):
        return "Action: %s" % ("SELL" if self.action == Decision.SELL else "BUY") + "for %s x %d" % (self.ticker, self.count)