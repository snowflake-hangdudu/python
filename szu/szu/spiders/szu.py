import scrapy
from ..items import Item
class SzuSpider(scrapy.Spider):
    name = "szu"
    allowed_domains = ["s.weibo.com"]
    start_urls = ["https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&_T_WM=87280250797&v_p=42"]
    def parse(self, response):
        print(response.text,'我是response')
       
        item = Item()
        list = response.xpath('//div[@action-type="feed_list_item"]')
        # //div[@data-v-485ecbd6][.//div[contains(@class, 'card-main')]]
        for i in list:
      
            item['type'] = 'weibo'
            item['title'] = i.xpath('./@mid')[0]
            item['url'] = mid2url(i.xpath('./@mid')[0])
            item['msg'] = i.xpath('.//p/text()')[0]
            item['icon_desc'] = ''
            item['hot_value'] = ''
            print(item,'我是item')
            yield item
            
            
        # print(list,'我是list')
        # print(response,'我是response')
def mid2url(mid):
    url = 'https://weibo.com/{}/{}'.format(mid[:mid.find('_')], mid[mid.find('_') + 1:])
    return url
      
   
