import pandas as pd
import yfinance as yf
import time

url = 'https://finance.yahoo.com/screener/predefined/top_mutual_funds/?offset=0&count=50'
data = pd.read_html(url)[0]

stk_list = data.Symbol
stock = yf.Ticker('KMKYX')
stock.history(period='max')
failed_list = []

for i in stk_list:
    try:
        print("process : " + i)
        stock = yf.Ticker(i)
        stock.history(period='max').to_csv('price_'+ i +'.csv' )
        time.sleep(1)

    except:
        failed_list.append(i)
        continue

