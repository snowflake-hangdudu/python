import urllib.request

print('运行了吗')

url = "https://blog.csdn.net/Pan_peter/article/details/1311520581"

headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

try:
     request = urllib.request.Request(url=url, headers=headers)
     response = urllib.request.urlopen(request)
     content = response.read().decode("utf-8")
     print(content.encode("gbk", errors="ignore").decode("gbk"))
except urllib.request.HTTPError:
     print('系统正在升级')

# except Exception as e:   这是处理全部异常的情况
#     print('系统正在升级')     



