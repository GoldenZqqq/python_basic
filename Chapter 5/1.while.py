# 初始条件
# n = 0
# while n < 5:
#     print("Hello Python!")
#     n += 1
#     print(n)


# 高斯求和
n = 1
result = 0
while n <= 10000:
    result += n
    n += 2  # 奇数求和
print(result)
