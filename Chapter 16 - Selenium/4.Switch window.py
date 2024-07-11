# 切换窗口
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
opt = Options()
opt.add_experimental_option("detach", True)  # 程序结束不自动关闭浏览器
opt.add_argument("--dsiable-blink-features=AutomationControlled")  # 隐藏浏览器痕迹
opt.page_load_strategy = "eager"
browser = webdriver.Chrome(service=service, options=opt)

url = "https://www.ruike1.com/forum.php?mod=forumdisplay&fid=47&filter=author&orderby=dateline"
browser.get(url)

time.sleep(3)
# //table[@id="threadlisttableid"]/tbody[3]/tr/th/a[2]
# //table[@id="threadlisttableid"]/tbody[4]/tr/th/a[2]
# //table[@id="threadlisttableid"]/tbody[5]/tr/th/a[2]
locator = (By.XPATH, '//table[@id="threadlisttableid"]/tbody[3]/tr/th/a[2]')
WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located(locator))

next_page = browser.find_element(
    By.XPATH, '//table[@id="threadlisttableid"]/tbody[3]/tr/th/a[2]'
)
for next in next_page:
    next.click()
    time.sleep(3)
    filename = browser.find_element(By.XPATH, '//*[@id="thread_subject"]').text
    break

""" 
# 浏览器窗口切换
driver.switch_to.window(driver.window_handles[0])  # 切换到第一个窗口

# 打开一个新的页面并切换至新页面
driver.switch_to.new_window('tab')

# 打开一个新的窗口并切换至新窗口
driver.switch_to.new_window('window')
"""
