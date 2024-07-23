# 找到Chrome浏览器的安装路径：
# C:\Program Files\Google\Chrome\Application\chrome.exe

# 在命令提示符输入下面命令创建配置一个浏览器
# chrome.exe --remote-debugging-port=8888 --user-data-dir="D:\selenium\ChromeProfile"

# 在chrome的快捷方式上右键，选择属性，快捷方式的目标栏后面加个空格加上以下命令：
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8888 --user-data-dir="D:\selenium\ChromeProfile"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service()
opt = Options()
opt.add_experimental_option("detach", True)  # 程序结束不自动关闭浏览器
opt.debugger_address = "127.0.0.1:8888"
browser = webdriver.Chrome(service=service, options=opt)
url = "https://www.douban.com/"

browser.get(url)
