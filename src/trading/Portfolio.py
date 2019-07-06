from typing import *
from .Asset import *
from .Source import *
from .Decision import *
class Portfolio(object):
    def __init__(self, assets: List[Asset], source: Source, cash=0):
        self.cash = cash
        self.assets = assets
        self.source = source
        
    
    def trade(self, strategy):
        decisions = strategy.decide(self.source, self)
        portfolio = self
        for decision in decisions:
            dCash = 0
            # print(portfolio.cash - decision.count * self.source.get_close(decision.ticker, 0))
            if decision.action == Decision.BUY:
                if decision.count * self.source.get_close(decision.ticker, 0) > portfolio.cash:
                    # print("Decision cannot be executed due to low cash %s" % decision)
                    continue
                else:
                    dCash = - decision.count * portfolio.source.get_close(decision.ticker, 0)
            elif decision.action == Decision.SELL:
                c = list(x.count for x in portfolio.assets if x.ticker == decision.ticker)[0]
                if c < decision.count:
                     dCash = c * portfolio.source.get_close(decision.ticker, 0) 
                else:
                     dCash = decision.count * portfolio.source.get_close(decision.ticker, 0) 
            # print(decision)
            v = portfolio.get_value()
            portfolio = Portfolio(
                list(asset.trade(decision) for asset in portfolio.assets), 
                self.source,
                portfolio.cash + dCash
            )
            # print("dV = %f" % (portfolio.get_value() - v))
        self.source.forward()
        # print("_____ Value: %f" % portfolio.get_value())
        return portfolio
    def simulate(self, strategy, iterations: int):
        portfolio = self
        for t in range(iterations):
            portfolio = portfolio.trade(strategy)
        return portfolio

    def get_value(self):
        return self.cash + sum(asset.get_value(self.source) for asset in self.assets)

    def __str__(self):
        return "Portfolio with cash %f" % self.cash + "\n%s" % "\n".join("\t%s: %d with value %f" % (x.ticker, x.count, self.source.get_close(x.ticker, 0)) for x in self.assets)
