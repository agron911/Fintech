import pandas as pd
import yfinance as yf
import time


url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]

stk_list = data.Symbol
stk_list

stk_basic_data = yf.Ticker('AAPL').info
stk_basic_data

info_columns = list(stk_basic_data.keys())

stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)

failed_list = []

for i in stk_info_df.index:
    try:
        print('processing: ' + i)

        info_dict = yf.Ticker(i).info

        columns_included = list(info_dict.keys())
        intersect_columns = [x for x in info_columns if x in columns_included]
        
        stk_info_df.loc[i,intersect_columns] = list(pd.Series(info_dict)[intersect_columns].values)
    
        time.sleep(1)
    except:
        failed_list.append(i)
        continue

stk_info_df.to_csv('text.csv')