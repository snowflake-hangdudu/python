import json
from scrapy_redis.spiders import RedisSpider
import scrapy
from ..items import Item


class ZhihupSpider(RedisSpider):
    name = "zhihup"
    allowed_domains = ["zhihu.com"]
    redis_key = 'zhihup:start_urls'
    # start_urls = ["https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true"]

    def parse(self, response):
        source = json.loads(response.text)
        for i in source['data']:
            item = Item()
            url = '' if i.get('target').get('id') is None else i.get('target').get('id')
            item['type'] = 'zhihu'
            item['title'] = '' if i.get('target').get('title') is None else i.get('target').get('title')
            item['url'] = f'https://www.zhihu.com/question/{url}'
            item['msg'] = '' if i.get('target').get('excerpt') is None else i.get('target').get('excerpt')
            item['icon_desc'] = ''
            item['hot_value'] = '' if i.get('detail_text') is None else i.get('detail_text')
            yield item



