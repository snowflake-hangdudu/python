import urllib.request
import urllib.parse
import json

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"

headers = {
 "Accept": "*/*",
  # "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cache-Control": "no-cache",
  "Connection": "keep-alive",
  "Cookie": "douban-fav-remind=1; _vwo_uuid_v2=DC475295A432C2CBF6CFB98B75DA3A674|7ae58dee240cb9db4976e19b0270ba04; ll=\"118282\"; bid=kt3OHFY3OLQ; __gads=ID=bb641c27a2c229dc-2296b38603e20089:T=1687915030:RT=1690164115:S=ALNI_MbzKK8cNg59ipDczi_-Z4E40fKSiA; __gpi=UID=00000c77277b46e1:T=1687915030:RT=1690164115:S=ALNI_MZwLQn65MFBUgNuN5PPTvoVhqiP4g; _pk_id.100001.4cf6=44c0d8065b9ff32f.1697781858.; __yadk_uid=p9YFqbBBQ6lThv5Ifj95xjbFDYNEe96K; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1697783012; __utmv=30149280.25820; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1704522707%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1433892384.1652766144.1704426089.1704522707.39; __utmb=30149280.0.10.1704522707; __utmc=30149280; __utmz=30149280.1704522707.39.38.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.870839992.1658917143.1704426089.1704522707.33; __utmb=223695111.0.10.1704522707; __utmc=223695111; __utmz=223695111.1704522707.33.32.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
  "Host": "movie.douban.com",
  "Pragma": "no-cache",
  "Referer": "https://movie.douban.com/",
  "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
  "X-Requested-With": "XMLHttpRequest"
}

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

#数据下载
#open方法默认下使用gbk的便民，如果想要保存汉字，需要指定编码utf-8
with open("豆瓣电影.json","w",encoding="utf-8") as fp:
    fp.write(content)

