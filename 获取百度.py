import urllib.request
import urllib.parse
import json
import  lxml.etree

#网站路径
url = "https://www.baidu.com/"

#网站的请求头
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# #获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")


tree = lxml.etree.HTML(content)

data = tree.xpath('//input[@id="su"]/@value')

print(data)


