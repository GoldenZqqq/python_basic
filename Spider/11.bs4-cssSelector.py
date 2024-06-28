# bs4 CSS选择器
from bs4 import BeautifulSoup

html = """
<table class="grid" width="100%" align="center">
<caption>搜索结果</caption>
  <tr align="center" style="height:30px;">
    <th width="20%">文章名称</th>
    <th width="40%">最新章节</th>
    <th width="15%">作者</th>
    <th width="9%">字数</th>
    <th width="10%">更新</th>
    <th width="6%">状态</th>
  </tr>
  <tr id="nr">
    <td class="odd"><a href="/10_10770/">斗罗大陆5重生唐三</a></td>
    <td class="even"><a href="/10_10770/41306831.html">第八百四十三章 盟友</a></td>
    <td class="odd">唐家三少</td>
    <td class="even">2376K</td>
    <td class="odd" align="center">2022-06-24</td> 
    <td class="even" align="center">连载</td> 
  </tr>
  <tr id="nr">
    <td class="odd"><a href="/22_22546/">斗罗大陆4终极斗罗（斗罗大陆IV终极斗罗）</a></td>
    <td class="even"><a href="/22_22546/33118436.html" target="_blank">后记</a></td>
    <td class="odd">唐家三少</td>
    <td class="even">6567K</td>
    <td class="odd" align="center">2021-05-20</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr id="nr">
    <td class="odd"><a href="/9_9331/">斗罗大陆</a></td>
    <td class="even"><a href="/9_9331/5967289.html">第二百三十六章 大结局，最后一个条件（全书完）</a></td>
    <td class="odd">唐家三少</td>
    <td class="even">9207K</td>
    <td class="odd" align="center">2018-10-18</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr id="nr">
    <td class="odd"><a href="/21_21532/">斗罗大陆IV终极斗罗</a></td>
    <td class="even"><a href="/21_21532/33118436.html" target="_blank">后记</a></td>
    <td class="odd">唐家三少</td>
    <td class="even">6096K</td>
    <td class="odd" align="center">2021-05-20</td>
    <td class="even" align="center">连载</td>
  </tr>
  <p>
    <a id="link1">Test</a>
    <c><b id="link2">Test</b></c>
  </p>
</table>
"""
soup = BeautifulSoup(html, "html.parser")

# 1.查找所有tr标签
# print(soup.select("tr"))

# 2.查找所有类名是odd的标签
# print(soup.select(".odd"))  # class='odd'

# 3.查找所有id是center的标签
# print(soup.select("#center"))

# 4.组合查找
# p标签下，包含属性值为 id=link2的标签
# print(soup.select("p #link2"))

# p标签下，所有的a标签
# print(soup.select("p a"))

# 5.查找属性值 target="_blank" 的a标签
# print(soup.select('a[target="_blank"]'))

# 6.获取属性值及文本
# 获取a标签的文本内容，及href的属性值
a = soup.select("a")
for i in a:
    print(i.get_text())
    print(i.get("href"))
