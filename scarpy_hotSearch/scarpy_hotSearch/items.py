# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScarpyHotsearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片的路径
    src = scrapy.Field()
    #图书名称
    name = scrapy.Field()
    #图书价格
    price = scrapy.Field()
    pass
