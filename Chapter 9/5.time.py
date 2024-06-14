import time

t = time.time()  # 时间戳：1970年1月1日至今的秒数
print(t)
t = time.localtime()  # 结构化的时间
print(t)
print(t.tm_year, type(t.tm_year))  # 获取
s = time.strftime("%Y-%m-%d %H:%M:%S")  # 格式化
print(s)

from my_package import my_tools

result = my_tools.get_time()
print(result)
