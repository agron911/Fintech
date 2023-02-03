import yfinance as yf
import pandas as pd
import time

url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]


stk_list = data.Symbol
stk = yf.Ticker('AAPL').info
stk2 = yf.Ticker('NVDA').info

A_info = list(stk.keys())
N_info = list(stk2.keys())
stk_info = pd.DataFrame(index = stk_list.sort_values(),columns=A_info)

intersec_col = [s for s in A_info if s in N_info]
stk_info.loc['NVDA',intersec_col]=list(pd.Series(stk2)[intersec_col].values)


stk_info.to_csv('1.csv')

