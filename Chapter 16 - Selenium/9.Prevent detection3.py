import undetected_chromedriver as uc
import time


# def run():
#     opt = uc.ChromeOptions()
#     opt.headless = True
#     browser = uc.Chrome(options=opt)
#     browser.get("https://www.taobao.com")
#     title = browser.title
#     print(title)


# if __name__ == "__main__":
#     run()

browser = uc.Chrome(use_subprocess=True)
browser.get("https://www.taobao.com")
time.sleep(2)
