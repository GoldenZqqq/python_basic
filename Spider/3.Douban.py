# 筛选豆瓣电影
import requests
import pprint

# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
# https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=
expected_rate = 9
sort = "time"
tag = "最新"
page = 201
for i in range(0, page, 20):
    url = "https://movie.douban.com/j/search_subjects"
    params = {
        "type": "movie",
        "tag": tag,
        "sort": sort,
        "page_limit": "20",
        "page_start": i,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    res = requests.get(url=url, headers=headers, params=params).json()["subjects"]

    for info in res:
        rate = info["rate"]
        title = info["title"]
        if float(rate) >= expected_rate:
            print(title, rate)
