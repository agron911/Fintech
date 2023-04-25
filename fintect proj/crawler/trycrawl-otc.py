import pandas as pd
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import random
print("Enter your otc stock code:")
codes = ['6152','5490','6160','2025','2516','4903','8255','6188','6143','9945']
# codes = ['6160']


for code in codes:
    
    try:

        filePath ='C:\\Users\\XPS-9365\\Downloads\\'+ code +'_history.csv'
        # filePath = Path('C:\\Users\\user\\Downloads\\'+ code+'_history.csv')
        os.chmod(filePath, 0o777)
        file = Path(filePath)
        os.remove(file)
    except Exception as e:
            print(e)
# code = input()
for code in codes:
    


    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("--start-maximized")


    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://www.cnyes.com/twstock/' + code + '/charts/technical-history')
    time.sleep(random.random())

    driver.execute_script("window.scrollTo(0, 1860)") 
    time.sleep(2)


    myw = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/button""")
    myw.click()

    time.sleep(random.random())

    myw = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[1]/button[8]""")
    myw.click()

    time.sleep(random.random())
    myw = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[3]/button[2]""")
    myw.click()

    time.sleep(2)
    myw = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/a/button""")
    myw.click()

    print(os.listdir)



    time.sleep(2)

    df = pd.read_csv('C:/Users/XPS-9365/Downloads/'+ code +'_history.csv')
    # df = pd.read_csv( 'C:/Users/user/Downloads/'+ code+'_history.csv')

    df = df[['日期','開盤','最高','最低','收盤',"成交張數"]]
    df.rename(columns={"日期":"Date","開盤":"Open","最高":"High","最低":"Low","收盤":"Close","成交張數":"Volume"},inplace=True)
    #df = df[['Date','Open','High','Low','Close',"Volume('000 shares)"]]
    #df = df.rename(columns={"Volume('000 shares)":"Volume"})
    df['Date1']=df.Date

    df.sort_values(by='Date',inplace=True)

    df.set_index('Date',inplace=True)
    df = df.rename(columns={"Date1":"Date"})

    df.to_csv('C:/Users/XPS-9365/Desktop/Fintech/fintect proj/crawler/stk2/'+code+'.txt',sep='\t')
    # df.to_csv('C:/Users/user/OneDrive/Fintech/fintect proj/crawler/stk2/'+code+'.txt',sep='\t')
    
    

    print(df)

