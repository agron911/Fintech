import yfinance as yf
import time
import pandas as pd

url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]

# 欄位『Symbol』就是股票代碼
stk_list = data.Symbol
stk_list
# 先測試一檔試看看
stock = yf.Ticker('AAPL')
failed_list = []

# 取得損益表，執行看看結果
stock.financials
stock.balance_sheet
stock.cashflow
for i in stk_list:
    try:
        print("process : " +i)
        stock = yf.Ticker(i)
        stock.financials.to_csv('profit_loss_account_'+ i +'.csv')
        stock.balance_sheet.to_csv('balance_sheet_'+ i +'.csv')
        stock.cashflow.to_csv('cashflow_'+ i + '.csv')
        time.sleep(1)
    except:
        failed_list.append(i)
        continue