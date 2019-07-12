from src.trading import *
import random
import sys

initial_cash = float(sys.argv[1])

random.seed(a=None)



source = Source("data/")
p = Portfolio([Asset(ticker, random.randint(0, 0)) for ticker in source.get_tickers()], source, initial_cash)

V0 = p.get_value()

print("Initial wealth: %f" % V0)

print(p)

agent = Agent(p, source)

strategy = NBStrategy() 
strategy.train(source, "text/training/positivity", "text/content")

for t in range(500):
    source.forward()

agent.simulate(strategy, 150)

print(agent.portfolio)
print("Initial value was %f" % V0)
print("End wealth: %f" % agent.portfolio.get_value())
print("Total return %f%%" % (100*(agent.portfolio.get_value() / V0 - 1)))
