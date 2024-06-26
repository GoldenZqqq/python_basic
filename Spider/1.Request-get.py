# request 网页采集
import requests

# 1.指定url
keyword = input("请输入要查询的关键字：")
# url = "https://www.sogou.com/web?query={}".format(keyword)
url = f"https://www.sogou.com/web?query={keyword}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# 2.网络请求，获得响应
response = requests.get(url=url, headers=headers)
print(response.text)

# 3.下载并保存
with open(keyword + ".html", "w", encoding="utf-8") as f:
    f.write(response.text)
    print(f"已下载...{keyword}")
