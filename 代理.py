import urllib.request
import urllib.parse
import json

#网站路径
url = ""

#网站的请求头
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器访问服务器

proxies = {
   #"http":"http://127.0.0.1:9000/",
}

handler = urllib.request.ProxyHandler(proxies=proxies)

response = urllib.request.build_opener(handler).open(request)


# #获取响应的数据





content = response.read().decode("utf-8")

#数据下载
#open方法默认下使用gbk的便民，如果想要保存汉字，需要指定编码utf-8
with open("test.json","w",encoding="utf-8") as fp:
    fp.write(content)

