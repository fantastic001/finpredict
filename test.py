from src.trading import *
import random

random.seed(a=None)

source = Source("data/")
p = Portfolio([Asset(ticker, random.randint(0, 10)) for ticker in source.get_tickers()], source)

V0 = p.get_value()

print("Initial wealth: %f" % V0)

print(p)

agent = Agent(p, source)

agent.simulate(MAStrategy(), 150)

print(agent.portfolio)
print("Initial value was %f" % V0)
print("End wealth: %f" % agent.portfolio.get_value())
print("Total return %f%%" % (100*(agent.portfolio.get_value() / V0 - 1)))
