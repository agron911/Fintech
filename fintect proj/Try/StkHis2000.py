import pandas as pd
import yfinance as yf
import time

url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]

stk_list = data.Symbol
stock = yf.Ticker('AAPL')
stock.history(period='max')
failed_list = []

for i in stk_list:
    try:
        print("process" + i)
        stock = yf.Ticker(i)
        stock.history(start = '2000-01-01').to_csv('price_'+ i +'.csv',colums= )
        time.sleep(1)

    except:
        failed_list.append(i)
        continue






