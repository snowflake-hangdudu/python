import scrapy
from ..items import Item
import urllib.request
import gzip
from lxml import etree
class SzuSpider(scrapy.Spider):
    name = "szu"
    allowed_domains = ["s.weibo.com"]
    start_urls = ["https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6"]

    def start_requests(self):
      url = "https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&Refer=realtime_weibo"
      headers = {
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
         "Accept-Encoding": "gzip, deflate, br",
         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
         "Cookie": "SINAGLOBAL=2264151323813.3413.1661842629731; SUB=_2AkMS_Fn3f8NxqwFRmfoRyG3kb41wwwzEieKkoKgsJRMxHRl-yT9kqnYdtRB6OXx3GLQ4fRvhCvqun5rQa1DOHLAmEdfB; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFY0Dr6h2yanHj20SjvarkH; _s_tentry=passport.weibo.com; Apache=5011448995157.987.1705039555756; ULV=1705039555851:3:1:1:5011448995157.987.1705039555756:1678526260928",
         "Referer": "https://s.weibo.com/realtime?q=%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&rd=realtime&tw=realtime&Refer=weibo_realtime",
         "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
         "Sec-Ch-Ua-Mobile": "?0",
         "Sec-Ch-Ua-Platform": "\"Windows\"",
         "Sec-Fetch-Dest": "document",
         "Sec-Fetch-Mode": "navigate",
         "Sec-Fetch-Site": "same-origin",
         "Sec-Fetch-User": "?1",
         "Upgrade-Insecure-Requests": "1",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
             }
          # 构造请求对象我是response2
      request = urllib.request.Request(url=url, headers=headers)

        # 发送请求并获取响应
      response = urllib.request.urlopen(request)

        # 检查是否使用了gzip压缩
      if response.info().get('Content-Encoding') == 'gzip':
            content = gzip.decompress(response.read()).decode('utf-8')
            # print(content, '我是content')
      else:
            content = response.read().decode('utf-8')
      content = etree.HTML(content)

      yield scrapy.Request(url=self.start_urls[0], callback=self.parse, meta={'content': content})
    def parse(self, response):
       
        response = response.meta['content']
        
        print(response, '我是response2')
       
        item = Item()
        list = response.xpath('//div[@action-type="feed_list_item"]')
        print(list, '我是list')
        
        for i in list:
            item['type'] = 'weibo'
            item['title'] = i.xpath('./@mid')[0]
            item['url'] = mid2url(i.xpath('./@mid')[0])
            item['msg'] = i.xpath('.//p/text()')[0]
            item['icon_desc'] = ''
            item['hot_value'] = ''
            print(item,'我是item')
            yield item
            
def mid2url(mid):
    url = 'https://weibo.com/{}/{}'.format(mid[:mid.find('_')], mid[mid.find('_') + 1:])
    return url
      
   
