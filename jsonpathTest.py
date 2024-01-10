#jsonpath只能解析本地的文件
import jsonpath
import json

obj = json.load(open('test.json','r',encoding='utf-8'))

# print(obj)

#拿取person里的name属性
data = jsonpath.jsonpath(obj,'$..*')

print(data)

