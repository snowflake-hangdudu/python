import json
import re
import scrapy
from ..items import Item
from scrapy_redis.spiders import RedisSpider


class KuaishoupSpider(RedisSpider):
    name = "kuaishoup"
    allowed_domains = ["kuaishou.com"]
    redis_key = 'kuaishoup:start_urls'

    # start_urls = ["https://www.kuaishou.com/?isHome=1"]

    def parse(self, response):
        # 用正则先把 items 数组解析出来
        pattern = r'"items":\s*(\[.*?\])'
        matches = re.search(pattern, response.text)
        _list = []
        if matches:
            items_str = matches.group(1)
            items = json.loads(items_str)
            # 存储数组
            _list = items

        # 循环数组找到每个热榜的对象
        for i in _list:
            pattern_item = rf'"{i["id"]}":\s*({{.*?}})'
            matches_item = re.search(pattern_item, response.text)
            item = Item()
            if matches_item:
                item_str = matches_item.group(1)
                _str = item_str + '}'
                _item = json.loads(_str)
                # print('--------------', _item)
                item['type'] = 'kuaishou'
                item['title'] = '' if _item['name'] is None else _item['name']
                item['url'] = mid2url(_item['photoIds']['json'][0], _item['id'])
                item['msg'] = ''
                item['icon_desc'] = '' if _item['tagType'] is None else _item['tagType']
                item['hot_value'] = '' if _item['hotValue'] is None else _item['hotValue']
                yield item
            else:
                print('数据出错')


def mid2url(json, id):
    url = f'https://www.kuaishou.com/short-video/{json}?streamSource=hotrank&trendingId={id}&area=homexxunknown'
    return url
