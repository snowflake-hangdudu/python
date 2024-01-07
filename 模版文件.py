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

# urllib.request.Request 类是用于创建 HTTP 请求的对象，可以通过该对象定制请求的各种属性。以下是涉及到的一些主要属性：
# url：指定请求的 URL。
# data：用于发送 POST 请求时传递的数据（如表单数据）。
# headers：设置请求头，包含一些附加信息，如 User-Agent、Cookie 等。
# method：指定请求的方法，常见的有 GET 和 POST。
# origin_req_host：指定原始请求的主机名或 IP 地址。
# unverifiable：表示该请求是否是可验证的（默认为 False）。
# host：指定请求的目标主机名或 IP 地址。
# type：指定请求的内容类型。
# timeout：设置超时时间，单位为秒。
# version：指定使用的 HTTP 版本。

# #获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

#数据下载
#open方法默认下使用gbk的便民，如果想要保存汉字，需要指定编码utf-8
with open("test.json","w",encoding="utf-8") as fp:
    fp.write(content)

