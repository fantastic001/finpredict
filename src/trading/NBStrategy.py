from .Strategy import *
from .Decision import *
from .PredictiveStrategy import *
from ..nn import * 
import numpy as np
from ..text_classification import * 
import pandas as pd 
import string
import os
class NBStrategy(PredictiveStrategy):

    def __init__(self):
        self.model = None
        self.tickers = []
        self.mapping = {}
        self.nb = None
        self.words = None
        self.news = [] 
    
    def clean_name(self, name):
        name = name.lower()
        name = "".join(c for c in name if c not in (string.ascii_lowercase + " "))
        ignore = ["inc", "incorporated", "corp", "corporation", "organization", "organisation", "org", "company"]
        return " ".join(w for w in name.split(" ") if w not in ignore)
    
    def get_all_news(self, news_path):
        res = []
        for t in sorted(os.listdir(news_path)):
            x = []
            for fp in os.listdir("%s/%s" % (news_path, t)):
                f = codecs.open("%s/%s/%s" % (news_path, t, fp), 'r', encoding='ascii', errors='ignore')
                x.append(f.read())
            res.append(x)
        return res
    
    def get_mentions(self, ticker, news, t):
        try:
            return len(list(c for c in news[t] if self.mapping[ticker] in c or ticker in c))
        except KeyError:
            return 0
    def train(self, source, training_text_dir_path, news_path):
        tickers = source.get_tickers()
        tickers_df = pd.read_csv("data/tickers/tickers.csv")        
        T = tickers_df.values.tolist()
        for t in T:
            self.mapping[t[0]] = self.clean_name(t[1])
        self.tickers = tickers
        self.nb, self.words = get_model_from_data(training_text_dir_path)
        self.news = self.get_all_news(news_path)
        x = [[tickers.index(ticker), p, self.get_mentions(ticker, self.news, source.get_time())] for ticker in tickers for p in [source.get_close(ticker, -source.get_time() + t) for t in range(1000)]]
        y = [p for ticker in tickers for p in [source.get_close(ticker, -source.get_time() + t+1) for t in range(1000)]]
        x = np.array(x)
        y = np.array(y)
        self.model = get_nn_regression_model(x,y)

    def predict(self, ticker, source):
        if self.model is None:
            raise TypeError("You have to train model before using this strategy.")
        else:
            return self.model.predict([[self.tickers.index(ticker), source.get_close(ticker, -1), self.get_mentions(ticker, self.news, source.get_time())]])