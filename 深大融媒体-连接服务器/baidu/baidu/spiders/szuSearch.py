import scrapy
import json
from ..items import Item


class SzusearchSpider(scrapy.Spider):
    name = "szuSearch"
    search = {
        '深圳大学': '深圳大学',
        'szu': 'szu',
        '深大': '深大'
    }
    allowed_domains = ["m.weibo.cn/"]
    start_urls = [
        "https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6"]

    def parse(self, response):
        source = json.loads(response.text)
        print('-----------------', source)
        # for i in source['data']['cards']:
        #     if i['card_type'] == 9:
        #         item = Item()
        #         _item = i['mblog']
        #         print('-----------------', _item['text'])
        #         # item['type'] = f"search:{self.search['深圳大学']}"
        #         item['title'] = _item['mid']
        #         item['url'] = mid2url(_item['mid'])
        #         # # item['msg'] = _item['text']
        #         # item['icon_desc'] = ''
        #         # item['hot_value'] = ''
        #         # yield item


def mid2url(mid):
    url = f'https://m.weibo.cn/detail/{mid}'
    return url
