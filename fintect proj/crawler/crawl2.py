from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.formula.api import ols
yf.pdr_override()

start = dt.datetime(2019, 1, 1)
end = dt.datetime(2019, 9, 30)


df = web.get_data_yahoo(['^TWII'],start, end)
df.to_csv(r'1.csv')



import pandas as pd
import numpy as np



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



daily_return1 = (close_df.diff()/close_df.shift(periods = 1)).dropna()
daily_return1.head()




daily_return2 = (open_df.diff()/open_df.shift(periods = 1)).dropna()
daily_return2.head()




fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,6))
daily_return1.plot(ax=ax[0])
ax[0].set_title("daily return_close")
daily_return2.plot(ax=ax[1])
ax[1].set_title("daily return_open")




d['X1']= 0
d['X2']= 0
d['X3']= 0 




print(d)




Q1 = ["2019-01", "2019-02", "2019-03"]
Q2 = ["2019-04", "2019-05", "2019-06"]
Q3 = ["2019-07", "2019-08", "2019-09"]
for i in Q1:
    d.loc[i,"X1"] = 1
for i in Q2:
    d.loc[i,"X2"] = 1
for i in Q3:
    d.loc[i,"X3"] = 1



print(d)



lrModel = LinearRegression()
y = d['Close'].values.reshape(-1, 1) 
x = d.iloc[:,6:]



est = sm.OLS(y, x)
est = est.fit()
print (est.summary())



x = sm.add_constant(x.to_numpy())



est = sm.OLS(y, x)
est = est.fit()
print (est.summary())
