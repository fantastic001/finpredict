from typing import *
from .Decision import *
from .Source import *
from .Portfolio import *
class Strategy(object):
    def __init__(self):
        pass
    
    def decide(self, source: Source, portfolio: Portfolio) -> List[Decision]:
        pass
      
