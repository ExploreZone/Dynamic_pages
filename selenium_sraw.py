#coding:utf-8

import requests
from bs4 import BeautifulSoup


url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"

web = requests.get(url)
# print web.content
soup = BeautifulSoup(web.content)
tag_con = soup.find("div",attrs={"id":"content"})
print tag_con.string