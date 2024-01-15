from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
# selenium语法全部改变，需重新查找资料

driver = webdriver.Chrome()
#访问网站
url = 'https://weibo.com/login.php'
driver.get(url)





#获取网页源码
content = driver.page_source
time.sleep(5)
#输入账号
zhanghao = driver.find_element(By.XPATH,'//*[@id="loginname"]')
zhanghao.send_keys('15551359775')
time.sleep(1)

#输入1密码
password = driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
password.send_keys('hangdudu')

#点击登录

login= driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()


#点击账号输入框


# 打印网页源码
# print(content,'我是网页源码')
time.sleep(1000)
driver.quit()



