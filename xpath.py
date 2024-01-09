import lxml.etree

#解析本地文件
tree = lxml.etree.parse('index.html')

#查看有属性的ul中的li的内容
data = tree.xpath('//ul[@id="city"]/li/text()')

print(data)
print(len(data))

#解析服务器响应的数据
# tree = lxml.etree.HTML(content)