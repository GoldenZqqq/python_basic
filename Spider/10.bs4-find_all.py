# bs4 find()和find_all()方法
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
</table>
"""
soup = BeautifulSoup(html, "html.parser")
# 1.获取第一个tr标签
# tr = soup.find("tr")
# print(tr)

# 2.获取所有的tr标签
# trs = soup.find_all("tr")
# for tr in trs:
#     print(tr)
#     print("--" * 30)

# 3.获取所有 id=nr 的tr标签
# trs = soup.find_all("tr", id="nr")
# trs = soup.find_all("tr", attrs={"id": "nr"})
# for tr in trs:
#     print(tr)
#     print("**" * 30)

# 4.将所有 class=odd align=center 的td标签提取出来
# tds = soup.find_all("td", class_="odd", align="center")
# tds = soup.find_all("td", attrs={"class": "odd", "align": "center"})
# for td in tds:
#     print(td.text)

# 5.获取所有属性值 target=_blank 的a标签的href属性
# a_tags = soup.find_all("a", target="_blank")
# for a_tag in a_tags:
#     print(a_tag["href"])
#     print(a_tag.get("href"))

# 6.获取所有小说名称、链接以及作者和日期信息，用列表的方式打印出来
trs = soup.find_all("tr", id="nr")
info = []
for tr in trs:
    tds = tr.find_all("td")
    link = tds[0].a["href"]
    name = tds[0].a.string
    author = tds[2].text
    date = tds[4].text
    info.append([link, name, author, date])
print(info)
