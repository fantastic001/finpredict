from .Strategy import *
from .Decision import *
from .PredictiveStrategy import *
from ..nn import * 
import numpy as np
class NNStrategy(PredictiveStrategy):

    def __init__(self):
        self.model = None
        self.tickers = []
    
    def train(self, source):
        tickers = source.get_tickers()
        self.tickers = tickers
        x = [[tickers.index(ticker), p] for ticker in tickers for p in [source.get_close(ticker, -source.get_time() + t) for t in range(1000)]]
        y = [p for ticker in tickers for p in [source.get_close(ticker, -source.get_time() + t+1) for t in range(1000)]]
        x = np.array(x)
        y = np.array(y)
        self.model = get_nn_regression_model(x,y)

    def predict(self, ticker, source):
        if self.model is None:
            raise TypeError("You have to train model before using this strategy.")
        else:
            return self.model.predict([[self.tickers.index(ticker), source.get_close(ticker, -1)]])