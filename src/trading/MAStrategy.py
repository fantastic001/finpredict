from .Strategy import *
from .Decision import *
from .PredictiveStrategy import *
class MAStrategy(PredictiveStrategy):
    
    def predict(self, ticker, source):
        prices = list(source.get_close(ticker, -x) for x in range(30))
        return sum(prices) / len(prices)
