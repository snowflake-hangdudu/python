#爬取电影天堂信息

url='https://www.dytt.to/index.htm'

import scrapy
from movie.items import MovieItem

class MovieSpider(scrapy.Spider):
 name = 'mv'
 allowed_domains = ['www.dytt.to']
 start_urls = ['https://www.dytt.to/index.htm']

 def parse(self, response):
  #第一页的名字和第二页的图片
  list = response.xpath('//div[@class="co_content2"]/ul/a')
  # print(list)

  url = 'https://www.dytt.to'
  # print(name_list,src_list)

  print('------------------------')
  for a in list:
      name = a.xpath('./text()').extract_first()
      src = a.xpath('./@href').extract_first()
      
      #第二页的地址
      src = url + src
      print(src)


      yield scrapy.Request(url=src,callback=self.parse_second)

 def parse_second(self,response):
   # print('++++++++++++++++++')
   print(response)
   # src = response.xpath('//div[Zoom]//img/@src').extract_first()
   # print(src,'src')


   



