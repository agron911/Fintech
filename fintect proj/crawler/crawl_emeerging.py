import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

res = requests.get('https://invest.cnyes.com/twstock/TWS/2025/history#fixed')
# print(res.content)

root = etree.HTML(res.content)
print(root)

content = root.xpath('//*[@id="_historyDataTable"]/div[2]/div[1]/div/button/span')


options = Options()
options.add_argument('--disable-notifications')

chrome = webdriver.Chrome('./web/chromedriver',chrome_options=options)

chrome.get('https://invest.cnyes.com/twstock/TWS/2025/history#fixed')
time.sleep(2)
chrome.execute_script("window.scrollTo(2,document.body.scrollHeight)")
# time.sleep(3)
time.sleep(1)
his = chrome.find_element(By.XPATH,'//*[@id="_historyDataTable"]/div[2]/div[1]/div/button')

his.click()
time.sleep(1)
max = chrome.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[3]/section[2]/div[2]/div[1]/div/div[2]/div[1]/button[8]')
max.click()
time.sleep(1)

# XPATH : //*[@id="_historyDataTable"]/div[2]/div[1]/div/button/span