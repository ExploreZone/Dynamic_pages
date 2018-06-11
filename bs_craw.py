#coding:utf-8

import requests
from bs4 import BeautifulSoup

url = "https://s.taobao.com/search?q=surface&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160228"

web =requests.get(url)
web =web.content
soup = BeautifulSoup(web, "html.parser")
for tag in soup.tagStack:
    print tag.encode('gbk', 'ignore')