#下载图书的图片，名称和价格



import scrapy
from scarpy_hotSearch.items import ScarpyHotsearchItem

class BaiduSpider(scrapy.Spider):
 #爬虫名称,用于运行爬虫的时候，使用的值
 name = 'dangdang'
 #运行访问的域名
 #如果是多页下载，那么必须跳转allowed_domains的范围，一般情况下只写域名
 allowed_domains = ['category.dangdang.com']
 #起始的url地址，指的是第一次要访问的域名
 start_urls = ['https://category.dangdang.com/cp01.01.02.00.00.00.html']

 url = 'https:'

 base_url = 'https://category.dangdang.com/pg'
 page = 1
#是执行了start_urls之后 执行的方法 方法中的response,就是返回的那个对象
 def parse(self, response):
  #pipelines 下载数据
  #items 定义数据结构
  print('开始爬取当当了')
  src_list = response.xpath('//div[@id="search_nature_rg"]//li/a/img/@data-original').extract()
  name_list = response.xpath('//div[@id="search_nature_rg"]//li/a/@title').extract()
  price_list = response.xpath('//div[@id="search_nature_rg"]//li/p[@class="price"]/span[1]/text()').extract()
  # print(src_list)
  # print(name_list)
  # print(price_list)

  li_list = response.xpath('//div[@id="search_nature_rg"]//li')
  for li in li_list:

   src =  li.xpath('./a/img/@data-original').extract_first()
   url = 'https:'
   #第一张图片和其他的图片的标签属性是不一样的，第一张图片的src可以使用，其他图片是data-original
   if(src):
    src = url + src 
   else:
    src = url +  li.xpath('./a/img/@src').extract_first() 
   name = li.xpath('./a/@title').extract_first()
   price = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()
   print(src,name,price)
   book  = ScarpyHotsearchItem(src=src,name=name,price=price)
   print(book)
   #获取一个book,就将book交给pipelines
   yield book
 #每一页的爬取的业务逻辑全是一样的，所以我们只需要将执行的那个页的请求再次调用parse方法
#第一页
# https://category.dangdang.com/cp01.01.02.00.00.00.html
# #第二页
# https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
# #第三页
# https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
   
   if(self.page < 10):
    self.page += 1
    url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

    
    #怎么调用parse方法
    #scrapy.Request就是scrapy发送请求的方法
    #url就是请求的url

    yield scrapy.Request(url,callback=self.parse)


  