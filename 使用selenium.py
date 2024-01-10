from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# selenium语法全部改变，需重新查找资料


browser = webdriver.Chrome()

#访问网站
url = 'https://www.baidu.com'
browser.get(url)



#获取网页源码
content = browser.page_source

button = browser.find_element(by='id', value='kw')


print(button)

#打印网页源码
# print(content)


time.sleep(10000)
browser.quit()


#chrome版本
# 版本 120.0.6099.217

