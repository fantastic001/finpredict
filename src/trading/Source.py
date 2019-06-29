from typing import *
class Source(object):
    def __init__(self, file_path: str):
        
        self.file_path = file_path
        
    
    def get_close(self, ticker: str, time: int) -> float:
        pass
    
    def get_open(self, ticker: str, time: int) -> float:
        pass
    
    def get_low(self, ticker: str, time: int) -> float:
        pass
    
    def get_high(self, ticker: str, time: int) -> float:
        pass
    
    def get_volume(self, ticker: str, time: int) -> float:
        pass
      
