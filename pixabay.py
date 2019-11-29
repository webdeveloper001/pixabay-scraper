import urllib
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup 
import csv                  
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Get ratings and reviews
class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"

urllib._urlopener = AppURLopener()
# urllib.urlretrieve("https://cdn.pixabay.com/photo/2019/09/16/13/30/landscape-4480996_960_720.jpg", "00000001.jpg")




url = 'https://pixabay.com/zh/images/search/'
session = requests.Session()
session.headers.update({
    'cache-control': 'no-cache',
     'Connection': 'keep-alive',
     'Cookie': 'lang=zh',
     'Accept-Encoding': 'gzip, deflate',
     'Host': 'pixabay.com',
     'Postman-Token': '70e520ed-f3a7-4cb2-b165-98cbd028defb,6ebcf650-f16f-45e1-b7ab-dccd7b2bf3a7',
     'Cache-Control': 'no-cache',
     'Accept': '*/*',
     'User-Agent': 'PostmanRuntime/7.17.1'
})
csv.register_dialect('myDialect1',
	  quoting=csv.QUOTE_ALL,
	  skipinitialspace=True)

f = open('pixabay.csv', 'w')
writer = csv.writer(f, dialect='myDialect1')
writer.writerow(['Name'])
r = session.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
items = soup.findAll('div', class_='item')
for item in items:
    if 'data-lazy' in item.find('img').attrs:
        path = item.find('img').attrs['data-lazy']
        urllib.urlretrieve(item.find('img').attrs['data-lazy'], path.split('/')[len(path.split('/')) - 1])
        writer.writerow([path.split('/')[len(path.split('/')) - 1]])
        print(item.find('img').attrs['data-lazy'])
