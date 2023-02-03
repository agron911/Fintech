import csv
import numpy as np
import pandas as pd
import talib 
import yfinance as yf
from talib import abstract

url = 'https://finance.yahoo.com/screener/predefined/top_mutual_funds/?offset=0&count=50'
data = pd.read_html(url)[0]
fund_list = data.Symbol

for i in fund_list:
    stk = yf.Ticker(i)

    data = stk.history(start = '2000-01-01')

    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    data.columns = ['open','high','low','close','volume']
    # 隨意試試看這幾個因子好了
    ta_list = ['MACD','RSI','MOM','STOCH']
    # 快速計算與整理因子
    for x in ta_list:
        output = eval('abstract.'+x+'(data)')
        output.name = x.lower() if type(output) == pd.core.series.Series else None
        data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
        data = data.set_index('key_0')
        
    data.to_csv('fund_'+i+'.csv')

# url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
# data = pd.read_html(url)[0]

# stk_list = data.Symbol
# stk = yf.Ticker('AAPL')


# info_columns = list(stk.history(period='max').keys())

# stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)

# 讀取所有
# for i in stk_info_df.index:
#     with open('price_'+ i +'.csv',newline='', encoding='utf-8') as csvfile:
#         rows = csv.reader(csvfile)
#         for row in rows:
#             print(row)

# col = []
# print(yf.Ticker('AAPL').history(period='max'))
# with open('price_AAPL.csv',newline='', encoding='utf-8') as csvfile:
#     rows = csv.reader(csvfile)
#     flag=1
#     for row in rows:
#         # print(row)
#         flag=flag+1
#         col = row
#         if(flag>=2):
#             break
# talib.ADX(df.High, df.Low, df.Close, timeperiod = 14)








