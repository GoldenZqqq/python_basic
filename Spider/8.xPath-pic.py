# 爬取图片网站
# 1.爬取图片页的网页源代码
import requests, os
from lxml import etree
import re

headers = {
    "Referer": "https://www.pexels.com/zh-cn/@1460862988/",
    "Cookie": 'cf_clearance=czWMrRsbucevN8dCugb5VQ8GKXMqj3akBRJMDP5TCxg-1704717166-0-2-78b79e30.3daf4839.de030419-0.2.1704717166; ab.storage.deviceId.5791d6db-4410-4ace-8814-12c903a548ba=%7B%22g%22%3A%2268ec4494-ce0c-8c29-3e15-2531bb26d496%22%2C%22c%22%3A1704717209070%2C%22l%22%3A1704717209070%7D; ab.storage.sessionId.5791d6db-4410-4ace-8814-12c903a548ba=%7B%22g%22%3A%22ab58b606-50d6-6841-90af-20d6b2583ce4%22%2C%22e%22%3A1704719026584%2C%22c%22%3A1704717209068%2C%22l%22%3A1704717226584%7D; active_experiment={"id":"paginatedMediumAds","name":"Paginate ads in medium suggestions","variant":{"id":"0","name":"control","weight":50,"isControl":true}}; b-user-id=5793c6b2-0054-c3d3-2677-8402a2374a63; _sp_ses.9ec1=*; _ga=GA1.1.1657217690.1704717166; _fbp=fb.1.1719488918749.756100010343149943; OptanonAlertBoxClosed=2024-06-27T11:48:44.516Z; __cf_bm=p.KtWtY4RAT_2BUTaNUNjEVeru0C3IoUR6iABOr8o2g-1719489013-1.0.1.1-XLlv2ZIaIF8ihrHin73r0.3ZBRKsbZCiNjeACwII7habFZXkV1uO7hVm02xySNm.I0UK85omCtn.zwnT4rHXQg; google-one-tap-skip-prompt=true; _ga_8JE65Q40S6=GS1.1.1719488911.2.1.1719489220.0.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+27+2024+19%3A53%3A40+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BSH&AwaitingReconsent=false; _pexels_session=a3%2B9kPJinJaSQ42etqBP5GZlDrQvapDXBMPDv7dl%2FbLI%2FRh8pf2QsmOBGzDWIaPZ%2BDSRdfhh7E7XzfzG9o7riCX7iC9XHir%2Fyly0bKtXELm%2BtFdNOpfQNnJDU%2BQCfOQ0RKLKr3d50%2FLHYNzVFzPdCtuG7Cyi2U5%2Bodg8ZtIl7PnC41kDPmD2--9QZrG3XYhO%2BzLP4I--eXXz%2FScNUFxhrRI%2BktN1sw%3D%3D; _sp_id.9ec1=0467b479-1fb2-4ab6-a8a3-e723931d76b4.1704717166.2.1719489225.1704717247.f7bfd3f1-3eae-4c63-bf44-58274db73576.0432bfd2-4f34-44d8-8647-4f56b440b648.339f0d08-eb9d-4dec-82d5-09d30b9f71e2.1719488910729.13',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
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
def download_pics(url, headers):
    links, titles = get_links(url, headers)
    if not os.path.exists(f"Spider/img"):
        os.mkdir("Spider/img")
    for num, link in enumerate(links):
        pic_content = requests.get(link, headers=headers).content
        with open(f"Spider/img/{titles[num]}.jpg", "wb") as f:
            f.write(pic_content)
            print(f"已下载...{titles[num]}")
