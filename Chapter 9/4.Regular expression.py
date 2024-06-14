import re

# 检测字符串是否为纯数字的字符串
# \d 匹配数字 \D 匹配非数字
result = re.match(r"\d+", "23523523523")
print(result)
# \w 匹配字母或数字或下划线
result = re.match(r"\w+", "a*8")
print(result)
# \s 匹配空白字符   \S 匹配非空白字符
# ^ 匹配字符串开头   $ 匹配字符串结尾
result = re.match(r"^\s+$", "   ")
print(result)
# . 匹配任意字符
result = re.match(r"^code\d-\d-.+$", "code5-2-random")
print(result)
# [] 区间，可选列表
result = re.match(r"^[a-zA-Z0-9]+$", "a123")
print(result)
# * 匹配0个或多个   + 匹配1个或多个
result = re.match(r"^abc{2,5}$", "abcccccc")
print(result)
# | 匹配左右任意一个
result = re.match(r"^a|b|c$", "d")
print(result)


# 身份证号
result = re.match(
    r"^\d{6}((20[01]\d)|(202[01234])|(1[89]\d\d))\d{7}[\dX]$", "12345620081234567X"
)
print(result)

# 手机号码
result = re.match(r"^1\d{10}$", "12345678901")
print(result)

from my_package import my_tools

print(my_tools.is_phone_number("13263734927"))
print(my_tools.is_id_number("310115199902226472"))
