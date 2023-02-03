from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time 


chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver =  webdriver.Chrome('chromedriver.exe')

driver.get('https://www.reddit.com/r/worldnews/top')


# driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/a[3]').click()
soup = BeautifulSoup(driver.page_source, 'html.parser')
all_soups = soup.find_all('h3')
running = 0 
threshold = 25
open_print = False
##
for each_soup in all_soups:
    if running == threshold:
        break
    # if each_soup.text == 'Pfizer is testing a pill that, if successful, could become first-ever home cure for COVID-19':
    #     open_print = True
    # if open_print == True:
    print(each_soup.text, '\n')
    running += 1
    
# ##
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# all_soups = soup.find_all('h3')

# running = 0 
# threshold = 25

# for each_soup in all_soups:
#     if running == threshold:
#         break
#     if open_print == True:
#         print(each_soup.text, '\n')
#         running += 1

# ##
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# all_soups = soup.find_all('h3')

# running = 0 
# threshold = 25
# open_print = False

# for each_soup in all_soups:
#     if running == threshold:
#         break
#     if each_soup == all_soups[0]:
#         open_print = True
#     if open_print == True:
#         print(each_soup.text, '\n')
#         running += 1

# ##
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# all_soups = soup.find_all('h3')

# running = 0 
# threshold = 25

# for each_soup in all_soups:
#     if running == threshold:
#         break
#     print(each_soup.text, '\n')
#     running += 1