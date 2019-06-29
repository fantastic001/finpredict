from src.trading import *

p = Portfolio([Asset("AAPL", 5), Asset("MSFT", 10)], Source(""))

source = Source("../data/")

print(p)

agent = Agent(p, source)

agent.simulate(RandomStrategy(), 150)

print(agent.portfolio)
