from typing import *
from .Strategy import *
class DoNothingStrategy(Strategy):
    
    def decide(self, source: Source, portfolio: Portfolio) -> List[Decision]:
        return []
      
