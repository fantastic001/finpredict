from typing import *
class Agent(object):
    def __init__(self, portfolio: Portfolio, source: Source):
        
        self.portfolio = portfolio
        
        self.source = source
        
    
    def trade(self, strategy: Strategy) -> None:
        pass
    
    def simulate(self, strategy: Strategy, iterations: int) -> None:
        pass
      