# 转义字符和原生字符串
# Python中转义字符
# raw 原生
# text = r"hello\world\npython"
# print(text)


# 正则表达式中的转义字符
import re

# text1 = "The subscription fee is $99 and the tax is $15"
# res = re.findall("\$\d+", text1)
# print(res)


# text3 = "abc888\water"
# res1 = re.findall("(\d+)\\\\", text3)
# res2 = re.findall(r"(\d+)\\", text3)
# print(res1)
# print(res2)

text4 = "<title >小汐泡芙【天宫舞曲】再现86版《西游记》嫦娥✿经典美 - AcFun弹幕视频网 - 认真你就输啦 (?ω?)ノ- ( ゜- ゜)つロ</title>"
res3 = re.findall(
    r"<title >(.*?) - AcFun弹幕视频网 - 认真你就输啦 \(\?ω\?\)ノ- \( ゜- ゜\)つロ</title>",
    text4,
)
print(res3)
