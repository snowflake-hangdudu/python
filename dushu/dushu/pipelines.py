# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DushuPipeline:
    def open_spider(self,spider):
        self.fp = open('dushu.json','w',encoding='utf-8')


    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    

    def close_spider(self,spider):
        self.fp.close()
# class MysqlPipeline:
    def open_spider(self,spider):
        settings = spider.settings
        self.host =  settings['DB_HOST']
        self.port =settings['DB_PORT']
        self.user =settings['DB_USER']
        self.password =settings['DB_PASSWORD']
        self.name =settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into dushu(name,src) values(%s,%s)'
        #执行sql
        self.cursor.execute(sql,(item['name'],item['src']))
        #提交
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()