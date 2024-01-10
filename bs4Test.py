from bs4 import BeautifulSoup

#通过解析本地文件，来讲bs4的基础语法进行讲解

#解析本地文件
#默认打开文件的格式为gbk。所以打开文件需要指定编码
soup = BeautifulSoup(open('index.html',encoding='utf-8'),'lxml')

# #根据标签名查找节点
# print(soup.ul)


# 获取标签的属性,
# print(soup.ul.attrs['id'])







#bs4的函数
# find()  返回第一个符合条件的值;特殊情况，属性为class,需要写成class_
# print(soup.find('ul',id = "city"))
# print(soup.find('ul', class_="hobby"))



# #find_all()  返回所有符合条件的值
# print(soup.find_all('ul'))

#select()  返回符合条件的值
print(soup.select('h1'))

#节点的属性,三种获取值的方法
obj = soup.select('h1')[0]
print(obj.attrs.get('class'))
# print(obj.get('class'))
# print(obj['class'])


#name是标签的名字，将属性值作为字典返回
