# import requests
# from io import StringIO
# import pandas as pd
# import numpy as np
# import datetime
# import time

# def crawl_price(date):
#     r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&type=ALL')
#     ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c):None for c in ' '})for i in r.text.split('\n') if len(i.split('",')) == 17 and i[0]!= '='])),header=0)
#     ret = ret.set_index('證券代號')
#     ret['成交金額']= ret['成交金額'].str.replace(',','')
#     ret['成交股數'] = ret['成交股數'].str.replace(',','')
#     return ret

# data = {}
# n_days = 5
# date = datetime.datetime.now()
# fail_cnt =0
# allow_continuous_fail_cnt = 5
# while len(data) < n_days:
#     print('parsing', date)
#     try:
#         data[date.date()] = crawl_price(date)
#         print('success!')
#         fail_cnt =0
#     except:
#         print('fail.check the date is holiday')
#         fail_cnt +=1
#         if fail_cnt == allow_continuous_fail_cnt:
#             raise
#             break
        
#     date -= datetime.timedelta(days=1)
#     time.sleep(3)

# # print(date[datetime.date(2021,3,26)])
import requests
from io import StringIO
import pandas as pd
import numpy as np

def crawl_price(date):
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&type=ALL')
    ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                        for i in r.text.split('\n') 
                                        if len(i.split('",')) == 17 and i[0] != '='])), header=0)
    ret = ret.set_index('證券代號')
    ret['成交金額'] = ret['成交金額'].str.replace(',','')
    ret['成交股數'] = ret['成交股數'].str.replace(',','')
    return ret
import datetime
import time

data = {}
n_days = 6
date = datetime.datetime.now()
fail_count = 0
allow_continuous_fail_count = 5
while len(data) < n_days:

    print('parsing', date)
    # 使用 crawPrice 爬資料
    try:
        # 抓資料
        data[date.date()] = crawl_price(date)
        print('success!')
        fail_count = 0
    except:
        # 假日爬不到
        print('fail! check the date is holiday')
        fail_count += 1
        if fail_count == allow_continuous_fail_count:
            raise
            break
    
    # 減一天
    date -= datetime.timedelta(days=1)
    time.sleep(5)