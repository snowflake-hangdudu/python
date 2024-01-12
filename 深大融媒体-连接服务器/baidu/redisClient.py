import redis

redis_conn = redis.Redis(host='192.168.0.100', port=6379, password='root', db=0)
# 百度
redis_conn.lpush('baidup:start_urls', 'https://top.baidu.com/board?tab=realtime')
# 抖音
redis_conn.lpush('douyinp:start_urls', 'https://www.douyin.com/aweme/v1/web/hot/search/list/')
# 快手
redis_conn.lpush('kuaishoup:start_urls', 'https://www.kuaishou.com/?isHome=1')
# 头条
redis_conn.lpush('toutiaop:start_urls',
                 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature=_02B4Z6wo00f01bDLjNwAAIDAuu1XdQ8-hCWw74hAAAmqv8jy7w1umYcO.4RrissEWGKM4xWIQgN7LHCeW9KJYBpL.3JSmcztP512EZ4JpsgzDNu2Z8CqN3cDLkO6PNrjulJpdPTuTaR5zLTKb2')
# 微博
redis_conn.lpush('weibop:start_urls', 'https://www.weibo.com/ajax/side/hotSearch')
# 知乎
redis_conn.lpush('zhihup:start_urls',
                 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true')
