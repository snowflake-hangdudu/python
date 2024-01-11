from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


url = "https://www.baidu.com"

driver.get(url)

#元素定位
button = driver.find_element(By.ID,"kw")


print(button.get_attribute('name'))









# 120.0.2210.121

time.sleep(10000)


