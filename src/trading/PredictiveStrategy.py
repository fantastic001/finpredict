from .Strategy import *
from .Decision import *
class PredictiveStrategy(Strategy):
    
    def decide(self, source: Source, portfolio: Portfolio) -> List[Decision]:
        tickers = source.get_tickers()
        decisions = []
        sorted_tickers = []
        for ticker in tickers:
            p = self.predict(ticker, source)
            P = source.get_close(ticker, 0)
            if P == 0:
                continue
            r = p / P
            sorted_tickers.append((ticker, r))
        sorted_tickers = sorted(sorted_tickers, key=lambda x: x[1])
        buys = list((ticker, r) for ticker, r in sorted_tickers if r > 1)
        sells = list((ticker, r) for ticker, r in sorted_tickers if r < 1)
        for ticker, r in sells:
            if r > 0:
                decisions.append(Decision.sell(ticker, int(10 / sells[0][1] / r)))
            else:
                decisions.append(Decision.sell(ticker, 100000)) # sell all
        for ticker, r in buys:
            decisions.append(Decision.buy(ticker, int(10*r/buys[-1][1])))
        return decisions

    def predict(self, ticker, source):
        raise NotImplementedError()
