import pandas as pd
import Talib 
import yfinance as yf

url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0'
data = pd.read_html(url)[0]

stk_list = data.Symbol
stk = yf.Ticker('AAPL')


info_columns = list(stk.history(period='max').keys())

stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)
failed_list = []
print('index: {0}, col:{1} '.format(stk_info_df.index,stk_info_df.columns))
for i in stk_info_df.index:
    try:
        # print("process" + i)
        his_dist=yf.Ticker(i).history(start='2000-01-01')
        col = list(his_dist.keys())
        intersect_columns = [x for x in info_columns if x in col]

        stk_info_df.loc[i,intersect_columns] = list(pd.Series(his_dist)[intersect_columns].values)
        talib.ADX(stk_info_df.High, stk_info_df.Low, stk_info_df.Close, timeperiod = 14).to_csv('t_'+i+'.csv')
        time.sleep(1)

    except:
        failed_list.append(i)
        continue
# print(stk_info_df)




# import pandas as pd
# import Talib
# # 改成 TA-Lib 可以辨識的欄位名稱
# data.columns = ['open','high','low','close','volume']
# # 隨意試試看這幾個因子好了
# ta_list = ['MACD','RSI','MOM','STOCH']
# # 快速計算與整理因子
# for x in ta_list:
#     output = eval('abstract.'+x+'(data)')
#     output.name = x.lower() if type(output) == pd.core.series.Series else None
#     data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
#     data = data.set_index('key_0')