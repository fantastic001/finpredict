from typing import *
from .Decision import *
from .Source import *
from .Portfolio import *
from ..ts import * 

class ARStrategy(object):
    def __init__(self):
        pass
    
    def decide(self, source: Source, portfolio: Portfolio) -> List[Decision]:
        res = []
        for ticker in source.get_tickers():
            mu, alpha, sigma2 = fit_model_simple([source.get_close(ticker, -dt) for dt in range(120)])
            c = mu // 100
            if c > 0:
                res.append(Decision.buy(ticker, c))
            else:
                res.append(Decision.sell(ticker, -c))
        return res
        
