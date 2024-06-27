# 爬取图片网站
# 1.爬取图片页的网页源代码
import requests, os
from lxml import etree
import re

headers = {
    "Cookie": '_ga=GA1.1.99208912.1699000115; cf_clearance=LUlgkGzeHr0PrqSXB0xUPQC86ZQsOgzs9z6p1VhiITk-1704260906-0-2-8375d37.a3bb5d59.40171179-0.2.1704260906; active_experiment={"id":"paginatedMediumAds","name":"Paginate ads in medium suggestions","variant":{"id":"1","name":"test","weight":50}}; OptanonAlertBoxClosed=2024-06-27T08:05:20.904Z; country-code-v2=CN; __cf_bm=3jGkWeipBjn0SH8plT73j7mrYWhW5Gd3rA6uopPIs4g-1719478421-1.0.1.1-1QRmcjHgdl2sKlOcWq3kYrsuA244NlP9AQKkzfxeoCa_B9ZbT6yZ7sylPD5gwIhRyCyxL35tdYTmhWDHRRvzRw; _sp_ses.9ec1=*; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+27+2024+16%3A59%3A09+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BSH&AwaitingReconsent=false; _sp_id.9ec1=3d9b377a-e5f8-470f-b98b-3fd079e7090a.1704260905.3.1719478790.1719476644.9315bc8e-34f2-4c8e-b165-a8d8fb8d3d9a.0be21f77-61ec-4059-91c8-e54b29aee1d9.0b061246-06f1-4f7f-8045-d29c940aefe6.1719478748452.2; _ga_8JE65Q40S6=GS1.1.1719478747.3.1.1719478790.0.0.0',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}
url = "https://www.pexels.com/zh-cn/"
# https://www.pexels.com/zh-cn/photo/26311714/


def get_links(url, headers):
    r = requests.get(url, headers=headers)
    # 2.解析网页源代码，提取图片的链接和图片的名字
    html = etree.HTML(r.text)
    links = html.xpath('//a[@data-testid="next-link"]//img/@src')
    titles = []
    # 获取url中的最后一段作为title
    # link: https://images.pexels.com/photos/25649820/pexels-photo-25649820.jpeg?auto=compress&cs=tinysrgb&w=750
    # title: pexels-photo-25649820
    for link in links:
        title = re.findall(r"/photos/\d+/([^/]+)\.", link)
        if len(title) > 0:
            titles.append(title[0])
    return links, titles


# 3.下载并保存这组图片
links = get_links(url, headers)
if not os.path.exist(f"Spider/img/"):
    os.mkdir("Spider/img")
for link in links:
    pic_content = requests.get(link, headers=headers).content
