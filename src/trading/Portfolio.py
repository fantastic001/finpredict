from typing import *
class Portfolio(object):
    def __init__(self, assets: List[Asset], source: Source):
        
        self.assets = assets
        
        self.source = source
        
    
    def trade(self, strategy: Strategy) -> Portfolio:
        pass
    
    def simulate(self, strategy: Strategy, iterations: int) -> Portfolio:
        pass
      