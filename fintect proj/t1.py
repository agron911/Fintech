from bs4 import BeautifulSoup
import requests
import time
url = "https://www.reddit.com/r/worldnews/hot"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
cnt =1


all_soups = soup.find_all('h3')

running = 0 
threshold = 50
print(all_soups)
for each_soup in all_soups:
    if running == threshold:
        break
    print(each_soup.text, '\n')
    running += 1
    time.sleep(3)
print('a')

# soup = BeautifulSoup(doc,'html.parser')
# rows = soup.find('table',class_='sortableSAQPoutputTable').find_all('tr')    
# for row in rows:
#     all_tds = row.find_all('td')
#     print(all_tds[0].text)
#     cnt+=1
#     if cnt>10:
#         break
# rows = soup.find('table',class_='sortableSAQPoutputTable').find(name='a').get('href')    
# print(rows)

# r2 = soup.find('table',class_='sortableSAQPoutputTable').find_all('a')
# for r in r2:
    # a = r2.find('a')
    # print(a[0]['href'])
# print(r2)
   
# url2 = "https://metacyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-6990"
# page2 = requests.get(url)
# soup2 = BeautifulSoup(page2.text,'html.parser')

# rows = soup2.find('div',class_='pageContentDynamic')
# print(rows.text)

# root = etree.HTML(page.content)
# res = root.xpath('/html/body/div[4]/text()')[9]
# print(res)


