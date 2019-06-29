from typing import *
from .Portfolio import *
from .Source import *
class Agent(object):
    def __init__(self, portfolio: Portfolio, source: Source):
        
        self.portfolio = portfolio
        
        self.source = source
        
    
    def trade(self, strategy) -> None:
        self.portfolio = self.portfolio.trade(strategy)
    
    def simulate(self, strategy, iterations: int) -> None:
        self.portfolio = self.portfolio.simulate(strategy, iterations)
      
