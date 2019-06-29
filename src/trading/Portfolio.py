from typing import *
from .Asset import *
from .Source import *
from .Decision import *
class Portfolio(object):
    def __init__(self, assets: List[Asset], source: Source):
        
        self.assets = assets
        
        self.source = source
        
    
    def trade(self, strategy):
        decisions = strategy.decide(self.source, self)
        portfolio = self
        for decision in decisions:
            portfolio = Portfolio(list(asset.trade(decision) for asset in portfolio.assets), self.source)
        return portfolio
    def simulate(self, strategy, iterations: int):
        portfolio = self
        for t in range(iterations):
            portfolio = portfolio.trade(strategy)
        return portfolio

    def __str__(self):
        return "Portfolio:\n%s" % "\n".join("\t%s: %d" % (x.ticker, x.count) for x in self.assets)
