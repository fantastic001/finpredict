from src.trading import *

source = Source("../data/")
p = Portfolio([Asset(ticker, 0) for ticker in source.get_tickers()], source)


print(p)

agent = Agent(p, source)

agent.simulate(RandomStrategy(), 150)

print(agent.portfolio)
