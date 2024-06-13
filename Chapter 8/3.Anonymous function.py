# 匿名函数
# fun = lambda a, b: a + b
# result = fun(5, 2)
# print(result)


a = [1, 2, 3, 4, 5]
result = map(lambda x: x**3, a)  # map函数用于映射
print(list(result))


# reduce  累加/累乘
from functools import reduce

result = reduce(lambda x, y: x * y, a)
print(result)


# filter  过滤
result = filter(lambda x: not x % 2, a)
print(list(result))

# 过滤0
a = [1, 2, 3, 40, 5, 6, 0, 6, 0, 5]
result = filter(lambda x: x, a)
print(list(result))

# 拼接列表每一项
result = int(reduce(lambda x, y: str(x) + str(y), a))
print(result)
