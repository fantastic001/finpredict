from typing import *
from .Decision import *
from .Source import *
class Asset(object):
    def __init__(self, ticker: str, count: int):
        
        self.ticker = ticker
        
        self.count = count

    def trade(self, decision: Decision):
        if decision.ticker == self.ticker:
            if decision.type == Decision.BUY:
                return Asset(self.ticker, self.count + decision.count)
            else:
                if decision.count > self.count:
                    return Asset(self.ticker, 0)
                else:
                    return Asset(self.ticker, self.count - decision.count)
        else:
            return Asset(self.ticker, self.count)
        
    
    def get_total_value(self, source: Source, n: int) -> float:
        return self.count * source.get_close(self.ticker, n)
      
