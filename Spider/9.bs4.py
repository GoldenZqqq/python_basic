# BS4基础语法
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/lacie" class="sister" id="link1">Lacie</a>,
<a href="http://example.com/elsie" class="sister" id="link2"><!-- Elsie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b><!-- Hey, buddy. Want to buy a used parser? --></b>
"""
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
# 获取标签
# print(soup.a)
# print(type(soup.a))
# # 获取标签的名称
# print(soup.a.name)

# 获取标签的属性值
# print(soup.a.attrs)
# print(soup.a["href"])
# print(soup.a.get("id"))


# 改变标签的属性值
# soup.a["class"] = "brother"
# print(soup.a)


# 获取标签的文本内容
# print(soup.a.string)
# print(soup.a.text)
# print(soup.a.get_text())
# print(type(soup.a.string))

# 获取注释部门文本内容
# from bs4.element import Comment
# print(soup.b.string)
# print(type(soup.b.string))

# 遍历文档树
body_tag = soup.body
# 返回所有子节点
# print(body_tag.contents)
# 返回所有子节点的迭代器
# for tag in body_tag.children:
#     print(repr(tag))

# 返回所有文本内容
# for tag in body_tag.strings:
#     print(repr(tag))

# 使用 stripped_strings 可以去除多余的空白内容
for tag in body_tag.stripped_strings:
    print(tag)
