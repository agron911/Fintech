from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.formula.api import ols

import pandas as pd
import numpy as np
yf.pdr_override()


start = dt.datetime(2018, 1, 1)
end = dt.datetime(2021, 3, 31)

df = web.get_data_yahoo(['5245.TW'],start, end)

df.to_csv('5245.csv')


d = pd.DataFrame(df)
print(d)

close_df = df["Close"]
open_df = df["Open"]

close_df.describe()
open_df.describe()

fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,6))
close_df.plot(ax=ax[0])
ax[0].set_title("Close")
open_df.plot(ax=ax[1])
ax[1].set_title("Open")