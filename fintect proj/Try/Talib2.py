import csv
import pandas as pd
import Talib 
import yfinance as yf
from talib import abstract

url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]

stk_list = data.Symbol
stk = yf.Ticker('AAPL')


info_columns = list(stk.history(period='max').keys())

stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = ['Open','High','Low','Close','Volume']
ta_list = ['MACD','RSI','MOM','STOCH']

df = df.astype('float')

ta_list = ['MACD','RSI']
ta_list = talib.get_functions()
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
        
        