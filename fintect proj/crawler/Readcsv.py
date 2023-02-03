
# import pandas as pd
# import yfinance as yf
# import time
# import matplotlib.pyplot as plt

# v= pd.read_csv('../Try/price_AAPL.csv')

# close_df = v["Close"]
# open_df = v["Open"]

# fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,6))
# close_df.plot(ax=ax[0])
# ax[0].set_title("Close")
# open_df.plot(ax=ax[1])
# ax[1].set_title("Open")



import pandas as pd
import yfinance as yf
import time

url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]
failed_list=[]
stk_list = data.Symbol
for i in stk_list:
    try:
        
        v= pd.read_csv('../Try/price_'+i+'.csv')
        print(i)
        close_df = v["Close"]
        open_df = v["Open"]

        fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,6))
        close_df.plot(ax=ax[0])
        ax[0].set_title("Close")
        open_df.plot(ax=ax[1])
        ax[1].set_title("Open")

    except:
        failed_list.append(i)
        continue
