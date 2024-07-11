from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service()
opt = Options()
# opt.add_argument("--dsiable-blink-features=AutomationControlled")  # 隐藏浏览器痕迹
# opt.add_experimental_option(
#     "excludeSwitches", ["enable-automation"]
# )  # 隐藏自动化浏览器控制标识的参数
opt.add_experimental_option("detach", True)  # 程序结束不自动关闭浏览器
driver = webdriver.Chrome(service=service, options=opt)

with open(
    "C:/Learn/python_basic/Chapter 16 - Selenium/stealth.min.js", "r", encoding="utf-8"
) as f:
    js = f.read()
    # print(js)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": js})

url = "https://bot.sannysoft.com/"
driver.get(url)
