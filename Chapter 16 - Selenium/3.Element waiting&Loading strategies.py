import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
opt = Options()
opt.add_experimental_option("detach", True)
opt.add_argument("--dsiable-blink-features=AutomationControlled")
opt.page_load_strategy = "none"

url = "https://www.ruike1.com/forum.php?mod=forumdisplay&fid=47&filter=author&orderby=dateline"
browser = webdriver.Chrome(service=service, options=opt)
# browser.implicitly_wait(5)
start = time.time()
browser.get(url)
end = time.time()
print(f"打开页面的时间：{end - start}")

for i in range(5):
    locator = (By.XPATH, f'//*[@id="fd_page_bottom"]/div/a[{i+1}]')
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator))
    except:
        print("未找到指定元素")
        browser.close()
        exit()
    next_page = browser.find_element(
        By.XPATH, f'//*[@id="fd_page_bottom"]/div/a[{i+1}]'
    )
    next_link = next_page.get_attribute("href")
    print(f"下一页链接：{next_link}")
    next_page.click()

browser.close()
