import scrapy

class BaiduSpider(scrapy.Spider):
 #爬虫名称,用于运行爬虫的时候，使用的值
 name = 'baidu'
 #运行访问的域名
 allowed_domains = ['http://www.baidu.com']
 #起始的url地址，指的是第一次要访问的域名
 start_urls = ['http://www.baidu.com/']


#是执行了start_urls之后 执行的方法 方法中的response,就是返回的那个对象
 def parse(self, response):
  print('开始爬取了')
  pass