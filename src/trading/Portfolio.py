from typing import *
from . import Strategy
class Portfolio(object):
    def __init__(self, assets: List[Asset], source: Source):
        
        self.assets = assets
        
        self.source = source
        
    
    def trade(self, strategy: Strategy) -> Portfolio:
        decisions = strategy.decide(source, self)
        portfolio = self
        for decision in decisions:
            portfolio = Portfolio(list(asset.trade(decision) for asset in portfolio.assets), source)
        return portfolio
    def simulate(self, strategy: Strategy, iterations: int) -> Portfolio:
        portfolio = self
        for t in range(iterations):
            portfolio = portfolio.trade(strategy)
        return portfolio
      
