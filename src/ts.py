import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
import spectrum
import math

def plot_log(series):
    series = pd.Series(series)
    lag_plot(series)
    plt.show()

def calculate_correlation(series):
    series = pd.Series(series)
    values = pd.DataFrame(series.values)
    dataframe = pd.concat([values.shift(1), values], axis=1)
    dataframe.columns = ['t-1', 't+1']
    result = dataframe.corr()
    return result["t+1"]["t-1"]

def fit_model_burg(series):
    AR, sigma, k = spectrum.arburg(series, 1)
    return AR, sigma, k

def fit_model_simple(series):
    series = pd.Series(series).map(lambda x: math.log(x))
    xhat = series.mean()
    xxhat = (series * series.shift(1)).mean()
    x2hat = (series ** 2).mean()
    mu = (xhat*x2hat - xxhat) / (x2hat - xhat**2)
    alpha =  (xxhat - mu*xhat) / x2hat
    sigma2 = abs(x2hat*(1 - alpha**2) - mu**2 - 2*mu*alpha * xhat)
    return mu, alpha, sigma2
