import json
from ..items import Item
import scrapy
from scrapy_redis.spiders import RedisSpider


class ToutiaopSpider(RedisSpider):
    name = "toutiaop"
    allowed_domains = ["toutiao.com"]
    redis_key = 'toutiaop:start_urls'

    # start_urls = [
    #     "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature=_02B4Z6wo00f01bDLjNwAAIDAuu1XdQ8-hCWw74hAAAmqv8jy7w1umYcO.4RrissEWGKM4xWIQgN7LHCeW9KJYBpL.3JSmcztP512EZ4JpsgzDNu2Z8CqN3cDLkO6PNrjulJpdPTuTaR5zLTKb2"]

    def parse(self, response):
        label_dict = {
            '': '',
            'hot': "热",
            'new': "新",
            'refuteRumors': "辟谣",
            'interpretation': '解读',
        }
        source = json.loads(response.text)
        for i in source['data']:
            item = Item()
            item['type'] = 'toutiao'
            item['title'] = '' if i.get('Title') is None else i.get('Title')
            item['url'] = '' if i.get('Url') is None else i.get('Url')
            item['msg'] = ''
            item['icon_desc'] = '' if label_dict.get(i.get('Label')) is None else label_dict.get(i.get('Label'))
            item['hot_value'] = '' if i.get('HotValue') is None else i.get('HotValue')
            yield item
