from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
# selenium语法全部改变，需重新查找资料


<<<<<<< HEAD
browser = webdriver.Chrome()

#访问网站
url = 'https://www.baidu.com'
browser.get(url)
=======
driver = webdriver.Chrome()


url = "https://www.baidu.com"

driver.get(url)

#元素定位
button = driver.find_element(By.ID,"kw")


print(button.get_attribute('name'))

>>>>>>> aa9e22f6b1f290f7a0a73c8770d633efe14c4e6f



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

