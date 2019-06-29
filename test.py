from src.trading import *
import random

source = Source("data/")
p = Portfolio([Asset(ticker, random.randint(0, 10)) for ticker in source.get_tickers()], source)

V0 = p.get_value()

print(p)

agent = Agent(p, source)

agent.simulate(MAStrategy(), 150)

print(agent.portfolio)
print("End wealth: %f" % agent.portfolio.get_value())
print("Total return %f%%" % 100*(agent.portfolio.get_value() / V0 - 1))
