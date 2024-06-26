# 在线翻译
import requests
import pprint

keyword = input("请输入你要翻译的关键字：")
query_url = "https://fanyi.sogou.com/reventondc/suggV3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

data = {
    "from": "auto",
    "to": "zh-CHS",
    "client": "web",
    "text": keyword,
    "uuid": "781da251-3a3e-47a3-956a-5bd51c7505a2",
    "pid": "sogou-dict-vr",
    "addSugg": "on",
}

res = requests.post(url=query_url, headers=headers, data=data)
result = res.json()["sugg"][0]["v"]
pprint.pprint(result)
