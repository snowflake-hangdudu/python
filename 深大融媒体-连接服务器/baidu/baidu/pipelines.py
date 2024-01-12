# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
from hashlib import md5
import pymysql


class BaiduPipeline:
    def __init__(self):
        self.redis_conn = None

    def open_spider(self, spider):
        self.redis_conn = redis.Redis(host='192.168.0.100', port=6379, password='root', db=0)

    def process_item(self, item, spider):
        m5 = md5()
        m5.update(item['title'].encode('utf-8'))
        flag = self.redis_conn.sadd(spider.name + ":md5", m5.hexdigest())
        if flag:
            return item

    def close_spider(self, spider):
        self.redis_conn.close()


class MySqlPipeline:
    def __init__(self):
        self.conn = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='192.168.0.100',
            port=3306,
            user='root',
            password='root',
            database='spider',
            charset='utf8'
        )

    def process_item(self, item, spider):
        if item is not None:
            cursor = self.conn.cursor()
            sql = "insert into spider(url,title,msg,type,icon_desc,hot_value) values (%s,%s,%s,%s,%s,%s)"
            val = (item['url'], item['title'], item['msg'], item['type'], item['icon_desc'], item['hot_value'])
            cursor.execute(sql, val)
            self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()
