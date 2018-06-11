#coding:utf-8

import time
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.get("https://s.taobao.com/search?q=surface&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160228")
time.sleep(7)
print driver.page_source.encode('gbk', 'ignore')
driver.get_screenshot_as_file("2.jpg")
print "success to create the screenshot & gather html"

driver.close()