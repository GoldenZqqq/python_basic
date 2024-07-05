# 爬取拉勾网
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.lagou.com"
service = Service()
opt = Options()
opt.add_experimental_option("detach", True)
opt.add_argument("--dsiable-blink-features=AutomationControlled")
browser = webdriver.Chrome(service=service, options=opt)
browser.maximize_window()
browser.get(url)

time.sleep(2)
open_select = browser.find_element(
    By.XPATH,
    "//li[@class='suggestCity']/span",
)
open_select.click()
time.sleep(2)
city_element = browser.find_element(
    By.CSS_SELECTOR,
    ".cityListBox__2NLde > ul > li:nth-child(2) > span",
)
city_element.click()

time.sleep(2)
# search_element = browser.find_element(By.ID, "search_input")
search_element = browser.find_element(By.CLASS_NAME, "search_input")
search_element.send_keys("Python爬虫工程师", Keys.ENTER)

time.sleep(3)
browser.close()
