import pandas as pd
import datetime

print("輸入你有的上櫃股票代號 enter your otc stock code:")
code = input()

df = pd.read_csv('C:/Users/XPS-9365/Downloads/'+ code +'.csv')

df = df[['Date','Open','High','Low','Close',"Volume('000 shares)"]]
df = df.rename(columns={"Volume('000 shares)":"Volume"})

df.sort_values(by='Date',inplace=True)

df.set_index('Date',inplace=True)
df.to_csv('./sk2/'+code+'.txt',sep='\t')

print(df)

# df.index = df.Date
# df.Date = datetime.datetime.strptime(df.Date,"%Y/%m/%d, %r").date()
# df.index = df.index.strftime("%Y/%m/%d , %r")

# df.Date = pd.to_datetime(df.Date,format='%Y/%m/%d')

# df.index = df.index.strftime("%Y/%m/%d , %r")

# df.Date = df.Date.astype(str)


# df.sort_values(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'],by='Date')
# print(df.sort_values(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'],key='Date'))