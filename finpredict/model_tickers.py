from finpredict.ts import * 
from finpredict.trading import * 
import pandas as pd
import numpy as np

def get_data():

    source = Source("data/", "2017")

    res = []

    for ticker in source.get_tickers():
        df = source.get_ticker(ticker)
        mu, alpha, sigma2 = fit_model_simple(df["adjClose"])
        res.append({
            "ticker": ticker,
            "mu": mu,
            "alpha": alpha,
            "sigma2": sigma2
        })

    x = pd.DataFrame(res)
    print(x)

    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    z_points = x["mu"]
    x_points = x["alpha"]
    y_points = x["sigma2"]
    ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv');
    plt.show()