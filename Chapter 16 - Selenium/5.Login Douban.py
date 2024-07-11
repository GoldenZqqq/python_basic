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
opt.page_load_strategy = "eager"
browser = webdriver.Chrome(service=service, options=opt)

url = "https://douban.com/"
browser.implicitly_wait(4)
browser.get(url)

time.sleep(3)
iframe = browser.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(iframe)
browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/ul[1]/li[2]").click()
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="username"]').send_keys("123456")
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("asdasgfas")
time.sleep(3)
browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[5]/a").click()

browser.switch_to.default_content()
time.sleep(3)
browser.close()
