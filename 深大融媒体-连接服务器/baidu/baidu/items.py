# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    msg = scrapy.Field()
    type = scrapy.Field()
    icon_desc = scrapy.Field()
    hot_value = scrapy.Field()
