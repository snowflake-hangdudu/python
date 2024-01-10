import urllib.request
import urllib.parse
import json
import requests

#网站路径
url = "https://www.baidu.com/s?"

data = {
    "wd": "北京"
}

#网站的请求头
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

response = requests.get(url=url,params=data,headers=headers)

content = response.text

print(content)




