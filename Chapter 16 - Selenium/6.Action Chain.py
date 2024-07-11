# 动作链
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

service = Service()
opt = Options()
opt.add_argument("--dsiable-blink-features=AutomationControlled")  # 隐藏浏览器痕迹
opt.add_experimental_option(
    "excludeSwitches", ["enable-automation"]
)  # 隐藏自动化浏览器控制标识的参数
opt.add_experimental_option("detach", True)  # 程序结束不自动关闭浏览器
opt.page_load_strategy = "eager"
browser = webdriver.Chrome(service=service, options=opt)

url = "https://www.12306.cn/index/index.html"
browser.implicitly_wait(5)
browser.maximize_window()

# temp_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
browser.get(url)


# 把鼠标悬停在车票上
time.sleep(2)
ticket_element = browser.find_element(By.XPATH, '//*[@id="J-chepiao"]/a')
ActionChains(browser).move_to_element(ticket_element).perform()

# 点击单程进入下一个页面
time.sleep(1)
one_way_element = browser.find_element(
    By.XPATH, '//*[@id="megamenu-3"]/div[1]/ul/li[1]/a'
)
ActionChains(browser).click(one_way_element).perform()

# 关闭弹窗
# time.sleep(2)
# pop_element = browser.find_element(
#     By.XPATH, '*[@id="qd_closeDefaultWarningWindowDialog_id"]'
# )
# ActionChains(browser).click(pop_element).perform()

# 输入出发地
time.sleep(1)
from_station = browser.find_element(By.XPATH, '//*[@id="fromStationText"]')
ActionChains(browser).click(from_station).pause(1).send_keys("婺源").pause(1).send_keys(
    Keys.ENTER
).perform()

# 输入目的地
time.sleep(1)
to_station = browser.find_element(By.XPATH, '//*[@id="toStationText"]')
ActionChains(browser).click(to_station).pause(1).send_keys("上海").pause(1).send_keys(
    Keys.ENTER
).perform()

# 选择日期
time.sleep(1)
# //*[@id="train_date"]
date_element = browser.find_element(By.XPATH, '//*[@id="train_date"]')
ActionChains(browser).click(date_element).pause(1).send_keys(
    Keys.ARROW_RIGHT, Keys.ARROW_RIGHT
).pause(1).send_keys(
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
    Keys.BACKSPACE,
).pause(
    1
).send_keys(
    "2024-07-17", Keys.ENTER
).perform()

# 勾选高铁
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="_ul_station_train_code"]/li[1]').click()

# 选择发车时间
time.sleep(1)
start_time_element = browser.find_element(By.XPATH, '//*[@id="cc_start_time"]')
Select(start_time_element).select_by_visible_text("18:00--24:00")

# 点击查询
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
