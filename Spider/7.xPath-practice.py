# xPath案例：爬取人生格言
# 1.获取网页源代码
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
url = "https://www.yjbys.com/juzi/lizhi/34566.html"


def get_content(url, headers):
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    # 2.解析网页源代码，提取内容
    html = etree.HTML(r.text)
    content = html.xpath('//div[@class="content"]/p/text()')
    title = content[0]
    del content[0]
    content = "".join(content)

    return title, content


# 3.爬取目录页的网页源代码
index_url = "https://www.yjbys.com/juzi/lizhi"
r = requests.get(index_url, headers=headers)
r.encoding = r.apparent_encoding

# 4.提取所有格言的链接
html = etree.HTML(r.text)
links = html.xpath('//div[@class="newlist"]//a/@href')

# 5.下载并保存所有格言
for link in links:
    title, content = get_content(link, headers)
    with open(f"Spider/txt/{title}.txt", "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(content + "\n\n")
        print(f"已下载...{title}")
