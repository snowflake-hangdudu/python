import scrapy
from ..items import Item
from scrapy_redis.spiders import RedisSpider


class BaidupSpider(RedisSpider):
    name = "baidup"
    allowed_domains = ["baidu.com"]
    # start_urls = ["https://top.baidu.com/board?tab=realtime"]
    redis_key = 'baidup:start_urls'

    def parse(self, response):
        list_selector = response.xpath("//div[@class='category-wrap_iQLoo horizontal_1eKyQ']")
        for one_selector in list_selector:
            item = Item()
            title = one_selector.xpath("div[2]/a/div/text()").extract()[0]
            url = one_selector.xpath("div[2]/a/@href").extract()[0]
            msg = one_selector.xpath("div[2]/div[2]/text()").extract()[0]
            icon_desc = one_selector.xpath("div[2]/a/div[2]/text()").extract()[0]
            hot_value = one_selector.xpath("div/div[2]/text()").extract()[0]
            item['type'] = 'baidu'
            item['title'] = '' if title is None else title
            item['url'] = '' if url is None else url
            item['msg'] = '' if msg is None else msg
            item['icon_desc'] = '' if icon_desc is None else icon_desc
            item['hot_value'] = '' if hot_value is None else hot_value
            yield item
