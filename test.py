from src.trading import *

p = Portfolio([Asset("AAPL", 5)], Source("")).trade(DoNothingStrategy())

print(p)
