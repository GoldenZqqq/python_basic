year = 2024  # 年份
month = 6
day = 7
week = "五"
weather = '阴'
temperature = 24.2

print("我是mia")
print(year, "年，我要减肥", sep="", end="\n\n")  # sep: 设置打印多个内容的分隔符
# end: 设置print执行结束后的操作
print(year, "年，我要读100本书", sep="", end="\n\n")
print(year, "年，我要去10个城市旅游", sep="", end="\n\n")
print("今天是 %d 年 %02d 月 %d 日，星期 %s ，天气 %s ，温度 %.1f 度" % (year, month, day, week, weather, temperature))