import json
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import Item


class WeibopSpider(RedisSpider):
    name = "weibop"
    allowed_domains = ["weibo.com"]
    redis_key = 'weibop:start_urls'
    # start_urls = ["https://www.weibo.com/ajax/side/hotSearch"]

    def parse(self, response):
        source = json.loads(response.text)
        for i in source['data']['realtime']:
            item = Item()
            item['type'] = 'weibo'
            item['title'] = '' if i.get('note') is None else i.get('note')
            item['url'] = '' if i.get('mid') is None else mid2url(i.get('mid'))
            item['msg'] = ''
            item['icon_desc'] = '' if i.get('icon_desc') is None else i.get('icon_desc')
            item['hot_value'] = '' if i.get('num') is None else i.get('num')
            yield item

    
def mid2url(mid):
    url = 'https://weibo.com/{}/{}'.format(mid[:mid.find('_')], mid[mid.find('_') + 1:])
    return url
