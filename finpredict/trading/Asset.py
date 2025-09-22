from typing import *
from .Decision import *
from .Source import *
class Asset(object):
    def __init__(self, ticker: str, count: int):
        
        self.ticker = ticker
        
        self.count = count

    def trade(self, decision: Decision):
        if decision.ticker == self.ticker:
            if decision.action == Decision.BUY:
                return Asset(self.ticker, self.count + decision.count)
            else:
                if decision.count > self.count:
                    return Asset(self.ticker, 0)
                else:
                    return Asset(self.ticker, self.count - decision.count)
        else:
            return Asset(self.ticker, self.count)
        
    
    def get_value(self, source: Source) -> float:
        return self.count * source.get_close(self.ticker, 0)
      
