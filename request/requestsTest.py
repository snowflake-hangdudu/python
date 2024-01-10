import requests

url = 'https://www.baidu.com/'

response = requests.get(url)
response.encoding = 'utf-8'

#一个类型和六个属性
print(type(response))

print(response.status_code)

print(response.headers)

print(response.cookies)

print(response.url)

print(response.text)

print(response.content)