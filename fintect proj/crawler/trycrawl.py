from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.formula.api import ols
import requests
from fake_useragent import UserAgent
import pandas as pd

import pandas as pd
import numpy as np
yf.pdr_override()

# headers = {
#         'user-agent' : UserAgent().random
#     }
# try:
#     res = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2",headers=headers,timeout=30)
#     res.close()
#     stock_list = pd.read_html(res.text)[0]
#     stock_list = stock_list.iloc[:,:1]
#     stock_list['code'] = stock_list.iloc[:,0].str.split(' ').str[0]
#     print(stock_list)

#     stock_list['cname'] = stock_list['code'].str.split(' ').str[1]
#     stock_list = stock_list[['code','cname']]
#     stock_list = stock_list.iloc[2:]

# except Exception as e:
#     print("Error raised in web crawing.")
#     print('\n ',e)
#     exit()


stock_list = pd.read_excel('./list.xls')
stock_list = stock_list.iloc[:,:1]
stock_list['code'] = stock_list.iloc[:,0].str.split('　').str[0]
all = stock_list.code

stock_list['cname'] = stock_list.iloc[:,0].str.split('　').str[1]
stock_list = stock_list[['code','cname']]
stock_list = stock_list.iloc[2:]
stock_list=stock_list.set_index('code').T.to_dict('string')
print(stock_list["1314"].cname)


start = dt.datetime(2005, 1,1)
end = dt.datetime(2023,12,24)

in_stocks_ch = ['4919','1314', '2485', '2353', '6216', '6168', '2399', '3062', '2516', '3443', 
'5490', '2324', '3356', '2337', '2002', '1471', '2484', '8104', '6160', '2025', '2374']

in_stocks_en = ['2330', '2511','1710', '6116', '2883', '1909', '2603', '3034','6152']


for i in in_stocks_ch:
    df = web.get_data_yahoo([i+'.TW'],start, end)
    # print(df.Date)
    # df = df.drop(columns=['Adj Close'])
    # print(df)
    try:
        df.index = df.index.strftime("%Y/%m/%d , %r")
        df.index = df.index.str.split(",").str[0]
        # df['Date'] = df.index
        df['OpenInt'] = df['Adj Close']
        df = df.drop(columns=['Adj Close'])

        # print(df.Open)
        df.to_csv('./stk2/'+ stock_list[i].cname+'.txt',sep='\t')
    except:
        continue;

for i in in_stocks_en:
    df = web.get_data_yahoo([i+'.TW'],start, end)
    # print(df.Date)
    df = df.drop(columns=['Adj Close'])
    # print(df)
    try:
        df.index = df.index.strftime("%Y/%m/%d , %r")
        df.index = df.index.str.split(",").str[0]
        df['Date'] = df.index

        # print(df.Open)
        df.to_csv('./stk2/'+ i+'.txt',sep='\t')
    except:
        continue;

df = web.get_data_yahoo(['^TWII'],start, end)
df = df.drop(columns=['Adj Close'])
# df.index.strftime("%Y/%M/%D")
df.index = df.index.strftime("%Y/%m/%d , %r")
df.index = df.index.str.split(",").str[0]

df['Date'] = df.index

df.to_csv('./stk2/TWII.txt',sep='\t')


for i in all:
    df = web.get_data_yahoo([i+'.TW'],start, end)
    # print(df.Date)
    df = df.drop(columns=['Adj Close'])
    # print(df)
    try:
        df.index = df.index.strftime("%Y/%m/%d , %r")
        df.index = df.index.str.split(",").str[0]
        df['Date'] = df.index

        # print(df.Open)
        df.to_csv('./stk2/'+ i+'.txt',sep='\t')
    except:
        continue;




# # Crawl one data
# df = web.get_data_yahoo(['6180.TW'],start, end)
# df = df.drop(columns=['Adj Close'])
# df.to_csv('./stk2/3086.csv')




# df1 = yf.Ticker(['5245.TW'])

# print(df1)
# df2 = df1.history(period='max')



# import requests
# from io import StringIO
# import pandas as pd
# import numpy as np

# datestr = '20180131'

# # 下載股價
# r = requests.post('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

# # 整理資料，變成表格
# df = pd.read_csv(StringIO(r.text.replace("=", "")), 
#             header=["5245" in l for l in r.text.split("\n")].index(True)-1)

# # 整理一些字串：
# df = df.apply(lambda s: pd.to_numeric(s.astype(str).str.replace(",", "").replace("+", "1").replace("-", "-1"), errors='coerce'))
# print(df)
# df.to_csv('5245.csv')
