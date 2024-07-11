# webdriver的基本操作
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = "https://www.baidu.com"
url1 = "https://jd.com"
service = Service()
opt = Options()
opt.add_experimental_option("detach", True)  # 程序结束不自动关闭浏览器
opt.add_argument("--dsiable-blink-features=AutomationControlled")  # 隐藏浏览器痕迹
browser = webdriver.Chrome(service=service, options=opt)
browser.maximize_window()
# browser.set_window_position(100, 20)
# browser.set_window_size(900, 900)
browser.get(url)

# time.sleep(1)
# browser.get(url1)

# time.sleep(1)
# browser.back()

# time.sleep(1)
# browser.forward()

# time.sleep(1)
# browser.refresh()

# time.sleep(1)
# page_text = browser.page_source
# print(page_text)

time.sleep(2)
# browser.close()  # 关闭一个标签
browser.quit()  # 关闭整个浏览器
