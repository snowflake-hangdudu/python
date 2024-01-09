import urllib.request
import urllib.parse
import json
import lxml.etree

# https://sc.chinaz.com/ppt/index.html
# https://sc.chinaz.com/ppt/index_2.html

def create_request(page):
    if(page ==1 ):
        url="https://sc.chinaz.com/ppt/index.html"
    else:
        url="https://sc.chinaz.com/ppt/index_" + str(page) + ".html"
    print(url)
    #网站的请求头

    for page in range(1,10):
        headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        }
        request = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode("utf-8")
        tree = lxml.etree.HTML(content)
        data = tree.xpath("//div[@class='moer-img-box clearfix']/img/@alt")

        #图片一般设计的网站进行懒加载
        data2 = tree.xpath("//div[@class='moer-img-box clearfix']/img/@src")
        print(data)
        print(data2)
        print(len(data))
        


create_request(1)



