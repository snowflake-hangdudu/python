from baidu.spiders.baidup import BaidupSpider
from baidu.spiders.douyinp import DouyinpSpider
from baidu.spiders.weibop import WeibopSpider
from baidu.spiders.kuaishoup import KuaishoupSpider
from baidu.spiders.toutiaop import ToutiaopSpider
from baidu.spiders.zhihup import ZhihupSpider
from baidu.spiders.szuSearch import SzusearchSpider
from scrapy.utils.project import get_project_settings

# 用哪个爬虫 在上面导入 在下面调用类 直接点运行就可以了
from scrapy.crawler import CrawlerProcess

if __name__ == '__main__':
    # 创建一个CrawlerProcess对象
    process = CrawlerProcess(get_project_settings())

    # 添加要运行的Spider到CrawlerProcess中
    # process.crawl(BaidupSpider)
    # process.crawl(DouyinpSpider)
    # process.crawl(KuaishoupSpider)
    # process.crawl(ToutiaopSpider)
    # process.crawl(WeibopSpider)
    # process.crawl(ZhihupSpider)
    process.crawl(SzusearchSpider)

    # 开始运行爬取任务
    process.start()
