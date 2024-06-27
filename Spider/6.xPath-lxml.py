from lxml import etree

# 读入本地的xml/html文件
# xml = etree.parse("Spider/xPath-test1.html")
# print(etree.tostring(xml).decode())


with open("Spider/xPath-test1.html", "r", encoding="utf-8") as f:
    text = f.read()
html = etree.HTML(text)
# 子节点和子孙节点的定位 / //
# result = html.xpath("/html/head/title/text()")
# result1 = html.xpath("//head/title/text()")
# result2 = html.xpath("//title/text()")
# print(result)
# print(result1)
# print(result2)

# 通过属性值定位标签
# result3 = html.xpath("//div[@class='song']")
# print(result3)
# result4 = html.xpath("//div[@class='song']/a[@target='_self']/text()")
# print(result4)
# result5 = html.xpath("//div[@class='song']/a[@class]/text()")
# print(result5)
# result6 = html.xpath('//div[@class="tang"]//a[@alt]/@href')[0]
# print(result6)


# 按照顺序来定位标签
# result7 = html.xpath('//div[@class="song"]/p[last()-1]/text()')[0]
# print(result7)

# 按照包含元素来定位
# result8 = html.xpath("//div[p and a]//text()")
# print(result8)

# 在对象中继续取值
result9 = html.xpath("//div[@class='song']")[0]
name = result9.xpath("./a[1]/@href")[0]
print(name)
