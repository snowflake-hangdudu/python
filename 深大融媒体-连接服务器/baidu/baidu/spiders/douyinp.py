import scrapy
import json
from scrapy_redis.spiders import RedisSpider
from ..items import Item


class DouyinpSpider(RedisSpider):
    name = "douyinp"
    allowed_domains = ["www.douyin.com"]

    redis_key = 'douyinp:start_urls'

    # start_urls = ["https://www.douyin.com/aweme/v1/web/hot/search/list/"]

    def parse(self, response, **kwargs):
        label_dict = {
            0: "无",
            1: "新",
            3: "热",
            4: "爆",
            5: "首发",
            8: "独家",
            16: "辟谣"
        }

        source = json.loads(response.text)
        for i in source['data']['word_list']:
            item = Item()
            item['type'] = 'douyin'
            item['title'] = '' if i.get('word') is None else i.get('word')
            item['url'] = '' if i.get('sentence_id') is None else f'https://www.douyin.com/hot/{i.get("sentence_id")}'
            item['msg'] = ''
            item['icon_desc'] = label_dict.get(0 if i.get('label') is None else i.get('label'))
            item['hot_value'] = '' if i.get('hot_value') is None else i.get('hot_value')
            if item['icon_desc'] is None:
                item['icon_desc'] = label_dict.get(0)

            yield item

        yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=False)
