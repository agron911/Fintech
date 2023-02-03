
# import requests
# from io import StringIO
# import pandas as pd
# import numpy as np

# def crawl_price(date):
#     r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&type=ALL')
#     ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
#                                         for i in r.text.split('\n') 
#                                         if len(i.split('",')) == 17 and i[0] != '='])), header=0)
# import datetime
# import time

# data = {}
# n_days = 9
# date = datetime.datetime.now()
# fail_count = 0
# allow_continuous_fail_count = 5
# while len(data) < n_days:

#     print('parsing', date)
#     # 使用 crawPrice 爬資料
#     try:
#         # 抓資料
#         data[date.date()] = crawl_price(date)
#         print('success!')
#         fail_count = 0
#     except:
#         # 假日爬不到
#         print('fail! check the date is holiday')
#         fail_count += 1
#         if fail_count == allow_continuous_fail_count:
#             raise
#             break
    
#     # 減一天
#     date -= datetime.timedelta(days=1)
#     time.sleep(5)


from IPython.display import display, clear_output
from urllib.request import urlopen
import pandas as pd
import datetime
import requests
import sched
import time
import json
import datetime as dt
import random
s = sched.scheduler(time.time, time.sleep)
def tableColor(val):
    if val > 0:
        color = 'red'
    elif val < 0:
        color = 'green'
    else:
        color = 'white'
    return 'color: %s' % color
def stock_crawler(targets):
    
    clear_output(wait=True)
    
    # 組成stock_list
    stock_list = '|'.join('tse_{}.tw'.format(target) for target in targets) 
    
    #　query data
    query_url = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch="+ stock_list
    data = json.loads(urlopen(query_url).read())
    print(data)
    # 過濾出有用到的欄位
    columns = ['c','n','z','tv','v','o','h','l','y']
    df = pd.DataFrame(data['msgArray'], columns=columns)
    df.columns = ['股票代號','公司簡稱','當盤成交價','當盤成交量','累積成交量','開盤價','最高價','最低價','昨收價']
    # df.insert(9, "漲跌百分比", 0.0) 
    
    # 新增漲跌百分比
    # for x in range(len(df.index)):
    #     if df['當盤成交價'].iloc[x] != '-':
    #         df.iloc[x, [2,3,4,5,6,7,8]] = df.iloc[x, [2,3,4,5,6,7,8]].astype(float)
    #         df['漲跌百分比'].iloc[x] = (df['當盤成交價'].iloc[x] - df['昨收價'].iloc[x])/df['昨收價'].iloc[x] * 100
    
    # 紀錄更新時間
    time = datetime.datetime.now()  
    # print("更新時間:" + str(time.hour)+":"+str(time.minute))
    
    # show table
    # df = df.style.applymap(tableColor, subset=['漲跌百分比'])
    df.to_csv('1101.csv')
    d = 600
    # start_time = datetime.datetime.strptime(str(time.date())+'9:30', '%Y-%m-%d%H:%M')
    # end_time =  datetime.datetime.strptime(str(time.date())+'13:30', '%Y-%m-%d%H:%M')
    start_time = dt.datetime(2017, 1, 1)
    end_time = dt.datetime(2021, 4, 4)
    # 判斷爬蟲終止條件
    # for i in range(d):
    #     s.enter(1, 0, stock_crawler, argument=(targets,))
    #     time.sleep(random.uniform(1,5))

    
# 欲爬取的股票代碼
stock_list = ['1101']

# 每秒定時器
s.enter(1, 0, stock_crawler, argument=(stock_list,))
s.run()