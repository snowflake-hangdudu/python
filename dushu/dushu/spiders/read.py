import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushu.items import DushuItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1188_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1188_\d+\.html"), 
                  callback="parse_item", 
                  follow=False),)

    def parse_item(self, response):
        
        img_list=response.xpath('//div[@class="bookslist"]//a/img')
        print(img_list)

        for i in img_list:
            name = i.xpath('./@alt').extract_first()
            src = i.xpath('./@data-original').extract_first()
            # print(name,src)
            book = DushuItem(name=name,src=src)
            yield book


       
