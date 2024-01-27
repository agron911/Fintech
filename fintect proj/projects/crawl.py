from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
import requests
from fake_useragent import UserAgent
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
from pathlib import Path
import random
import time
import wx

yf.pdr_override()
from stats_func import *



start = dt.datetime(2000, 1,1)
end = dt.datetime(2023,12,24)

long_tail_stk = {}

def crawl_all_ch(self):

    International_stock = pd.read_csv("international.txt")
    for i in International_stock['code']:
        df = web.get_data_yahoo([i],start, end)
        df = df.drop(columns=['Adj Close'])
        # df.index.strftime("%Y/%M/%D")
        df.index = df.index.strftime("%Y/%m/%d , %r")
        df.index = df.index.str.split(",").str[0]
        df['Date'] = df.index
        df.to_csv('./stk2/'+i+'.txt',sep='\t')


        print("Crawl:", i)

    stock_list = pd.read_excel(os.getcwd()+'/adjustments/list.xls')
    stock_list = stock_list.iloc[:,:1]
    stock_list['code'] = stock_list.iloc[:,0].str.split('　').str[0]
    all = stock_list.code

    df = web.get_data_yahoo(['^TWII'],start, end)
    df = df.drop(columns=['Adj Close'])
    # df.index.strftime("%Y/%M/%D")
    df.index = df.index.strftime("%Y/%m/%d , %r")
    df.index = df.index.str.split(",").str[0]
    df['Date'] = df.index

    df.to_csv('./stk2/TWII.txt',sep='\t')

    num=1
    print("ALL", all)
    for i in all:

        
        if num==950:
            break
        num+=1
        try:
            df = web.get_data_yahoo([i+'.TW'],start, end)
        except Exception as e:
            print("web get yahoo error:", str(e))
        df = df.drop(columns=['Adj Close'])
        try:
            df.index = df.index.strftime("%Y/%m/%d , %r")
            df.index = df.index.str.split(",").str[0]
            df['Date'] = df.index
            self.frame.input6.SetValue("" + i)

            # print(df.Open)
            print("Stock code : ", i)
            if long_tail(df):
                df.to_csv('./stk2/'+i+'_long_tail.txt',sep='\t')
                long_tail_stk[i] = df
                print("LONG_TAIL", long_tail_stk[i])

            df.to_csv('./stk2/'+ i+'.txt',sep='\t')
        except Exception as e:
            print(str(e))
            continue;

def crawl_all_otc(self):
    codes = pd.read_csv("otc.txt")
    # codes = ['5009','1108','3293','6152','5490','6160','2025','2516','4903','8255','6188','6143','9945']

    for code in codes['code']:
        
        try:
            s = os.getcwd()
            user_path = s.split("\\")[0]+ os.sep + s.split("\\")[1] + os.sep + s.split("\\")[2] + os.sep
            user_path_download  = user_path + "Downloads\\"
            # filePath ='C:\\Users\\XPS-9365\\Downloads\\'+ code +'_history.csv'
            filePath = Path(user_path_download + code+'_history.csv')
            os.chmod(filePath, 0o777)
            file = Path(filePath)
            os.remove(file)
        except Exception as e:
                print(e)
    # code = input()
    for code in codes:
        

            
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 

        service = Service(executable_path='./chromedriver.exe')
        options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(options=options, service=service)

        driver.get('https://www.cnyes.com/twstock/' + code + '/charts/technical-history')
        time.sleep(random.random())

        driver.execute_script("window.scrollTo(0, 1910)") 
        time.sleep(5)

        click_date = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/button""")
        click_date.click()
        time.sleep(2)

        time_value = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[2]/div[1]/input""")
        print("MINMIN:", time_value.get_attribute("min"))
        mindate = "2000-01-01"
        driver.execute_script("arguments[0].setAttribute('min', arguments[1])", time_value, mindate)
        print("MINMIN:", time_value.get_attribute("min"))
        time_value.send_keys(mindate)
        print("value:", time_value.get_attribute("value"))


        time.sleep(1)

        apply = driver.find_element(By.XPATH, """//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[3]/button[2]""")
        apply.click()

        time.sleep(3)           
        download = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/a/button""")
        download.click()

        print(os.listdir)

        time.sleep(1)

        # df = pd.read_csv('C:/Users/XPS-9365/Downloads/'+ code +'_history.csv')
        df = pd.read_csv( user_path_download + code+'_history.csv')

        df = df[['日期','開盤','最高','最低','收盤',"成交張數"]]
        df.rename(columns={"日期":"Date","開盤":"Open","最高":"High","最低":"Low","收盤":"Close","成交張數":"Volume"},inplace=True)
        #df = df[['Date','Open','High','Low','Close',"Volume('000 shares)"]]
        #df = df.rename(columns={"Volume('000 shares)":"Volume"})
        df['Date1']=df.Date

        df.sort_values(by='Date',inplace=True)

        df.set_index('Date',inplace=True)
        df = df.rename(columns={"Date1":"Date"})

        # df.to_csv('C:/Users/XPS-9365/Desktop/Fintech/fintect proj/crawler/stk2/'+code+'.txt',sep='\t')
        df.to_csv(s + '\\stk2\\'+code+'.txt',sep='\t')
        
        

        print(df)