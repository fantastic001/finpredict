from typing import *
from .Strategy import *
import random
class RandomStrategy(Strategy):
    
    def decide(self, source: Source, portfolio: Portfolio) -> List[Decision]:
        n = random.randint(0, 20)
        decisions = []
        for i in range(n):
            ticker = random.choice(source.get_tickers())
            count = random.randint(1, 10)
            x = random.choice([Decision.buy(ticker, count), Decision.sell(ticker,count)])
            decisions.append(x)
        return decisions
      
