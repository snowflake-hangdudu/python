#通过登录 进入到主页面

#通过登录接口，登录需要很多参数
# __VIEWSTATE: owM9yBhA4qoCxCeL8qPrj/VBUNvVqqKpfdyunqQVz6UaXtQPr52oozdGTfIhv9xaYDMJJhllxsqvfjzPuuB8Ep8hC6aE9uKIShj1bP+2uwuNbnKdmOFbWzeCaC7O9fhkFphSeDmOkT1wISqMXtnRW9muYd8=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 15551359775@163.com
# pwd: 123456
# code: 2UAX
# denglu: 登录

#_VIEWSTATE,__VIEWSTATEGENERATOR会变化

#难点 _VIEWSTATE,__VIEWSTATEGENERATOR会变化；验证码

#_VIEWSTATE,__VIEWSTATEGENERATOR在页面源码中，需要获取页面源码并解析

import requests

#登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

response = requests.get(url=url,headers=headers)

content = response.text

# print(content)

#解析网站源码

from bs4 import BeautifulSoup
soup = BeautifulSoup(content,'lxml')

#获取_VIEWSTATE,__VIEWSTATEGENERATOR
soup.select('#__VIEWSTATE')[0].attrs.get('value')
soup.select('#__VIEWSTATEGENERATOR')[0].get('value')

# print(soup.select('#__VIEWSTATE')[0].attrs.get('value'))
# print(soup.select('#__VIEWSTATEGENERATOR')[0].get('value'))

#获取验证码图片地址
soup.select('#imgCode')[0].attrs.get('src')
# print(soup.select('#imgCode')[0].attrs.get('src'))
code_url = 'https://so.gushiwen.cn'+soup.select('#imgCode')[0].attrs.get('src')

#下载图片,有坑,涉及到验证码问题，使用request，导致验证码更新，填写的验证码不对
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')
# code_name = input('请输入验证码')

session = requests.session()
#获取验证码的内容
response_code = session.get(code_url)

content_code = response_code.content

with open('code.jpg','wb') as fp:
    fp.write(content_code)

code_name = input('请输入验证码')
# import pytesseract
# #识别验证码
# code_name = pytesseract.image_to_string('code.jpg')

print(code_name)
#登录
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data = {
    '___VIEWSTATE': soup.select('#__VIEWSTATE')[0].attrs.get('value'),
'__ VIEWSTATEGENERATOR': soup.select('#__VIEWSTATEGENERATOR')[0].get('value'),
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': '15551359775@163.com',
'pwd': 'hangdudu',
'code': code_name,
'denglu': '登录',
}

response = session.post(url=url,headers=headers,data=data)

content = response.text
with open('古诗文.html','w',encoding='utf-8') as fp:
    fp.write(content)
print(content)

