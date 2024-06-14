import random

# 生成随机小数
a = random.random()
print(a)
# 生成随机整数
a = random.randint(1, 200)
print(a)

# 获取列表中的随机元素
list1 = [1, 2, 3, 4, 5, 6]
print(list1[random.randint(0, len(list1) - 1)])
print(random.choice(list1))
print(random.choice("hello"))

# 生成一个随机验证码
from my_package import my_tools

print(my_tools.generate_valid_code(5))


# 打乱原列表
random.shuffle(list1)
print(list1)
