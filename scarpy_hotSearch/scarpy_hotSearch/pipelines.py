# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



#如果想使用管道的话，那么就必须在setting中开启管道
class ScarpyHotsearchPipeline:
    #item就是yield后面的book对象

    #以下这种方法不推荐，因为每传递过来一个对象，那么久打开一次文件，对文件的操作过于频繁
    # def process_item(self, item, spider):
    #     #write方法必须要写一个字符串，不能是其他的对象
    #     with open('book.json','a',encoding='utf-8') as fp:
    #         fp.write(str(item))
    #     return item

    #在爬虫文件开启之前，执行的方法
    def open_spider(self,spider):
        self.f = open('book.json', 'w', encoding='utf-8')
        print('+++++++++++++++++++++++')




    def process_item(self, item, spider):
        self.f.write(str(item) + '\n')

        return item
    

    #在爬虫文件执行完知乎，执行的方法
    def close_spider(self,spider):
        print('-----------------------')
        self.f.close()
        pass
    

import urllib.request
import os
from urllib.request import urlretrieve  
    #多条管道开启
        #1.定义管道类
        #2.在setting中开启管道

class dangdangDownLoadPipeline:

   def process_item(self, item, spider):
    url = item.get('src')  
    print(url, 'url')
    
    # 清理文件名  
    filename = item.get('name')
    filename = filename.replace('/', '_')
    filename = filename.replace('\\', '_')
    filename = filename.replace(':', '_')
    filename = filename.replace('*', '_')
    filename = filename.replace('?', '_')
    filename = filename.replace('"', '_')
    filename = filename.replace('<', '_')
    filename = filename.replace('>', '_')
    filename = filename.replace('|', '_')
    
    # 拼接路径  
    save_dir = './books'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    filename = os.path.join(save_dir, filename) + '.jpg'  

    print(filename, 'filename') 
    
    urlretrieve(url, filename)  

    return item
