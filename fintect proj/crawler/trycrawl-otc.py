import pandas as pd
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
print("Enter your otc stock code:")
# codes = ['5490','6160','6152','2025','2516']
# codes = ['6160']
code = input()
# for code in codes:
    

#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument("--test-type")

#     driver = webdriver.Chrome(chrome_options=options)


#     driver.get('https://invest.cnyes.com/twstock/TWS/' + code + '/history#fixed')
#     time.sleep(2)

#     driver.execute_script("window.scrollTo(0, 1050)") 
#     # time.sleep(1)


#     myw = driver.find_element(By.XPATH,"""/html/body/div[1]/div[1]/div[2]/div[3]/section[2]/div[2]/div[1]/div/button""")
#     myw.click()

#     # time.sleep(1)

#     myw = driver.find_element(By.XPATH,"""/html/body/div[1]/div[1]/div[2]/div[3]/section[2]/div[2]/div[1]/div/div[2]/div[1]/button[8]""")
#     myw.click()

#     time.sleep(2)
#     myw = driver.find_element(By.XPATH,"""/html/body/div[1]/div[1]/div[2]/div[3]/section[2]/div[2]/div[1]/div/div[2]/div[3]/button[2]""")
#     myw.click()

#     time.sleep(3)
#     myw = driver.find_element(By.XPATH,"""/html/body/div[1]/div[1]/div[2]/div[3]/section[2]/div[2]/div[1]/a/button""")
#     myw.click()

#     # os.rename('C:/Users/XPS-9365/Downloads/'+ code +'_history.csv', code+'.csv')
#     print(os.listdir)
#     os.rename('C:/Users/user/Downloads/'+ code +'_history.csv', 'C:/Users/user/Downloads/'+code+'.csv')




df = pd.read_csv('C:/Users/XPS-9365/Downloads/'+ code +'.csv')
# df = pd.read_csv( 'C:/Users/user/Downloads/'+ code+'.csv')

df = df[['Date','Open','High','Low','Close',"Volume('000 shares)"]]
df = df.rename(columns={"Volume('000 shares)":"Volume"})
df['Date1']=df.Date

df.sort_values(by='Date',inplace=True)

df.set_index('Date',inplace=True)
df = df.rename(columns={"Date1":"Date"})

df.to_csv('C:/Users/XPS-9365/Desktop/Fintech/fintect proj/crawler/stk2/'+code+'.txt',sep='\t')
# df.to_csv('C:/Users/user/OneDrive/Fintech/fintect proj/crawler/stk2/'+code+'.txt',sep='\t')

print(df)

