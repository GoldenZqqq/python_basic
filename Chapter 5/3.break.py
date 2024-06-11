# while True:
#     print(111)
#     name = input("请输入你的名字：")
#     if name == "mia":
#         print("mia欢迎回家")
#         break
#     else:
#         print("mia不在家，你一会儿再来吧")

# for i in range(10):
#     if i > 0 and i % 3 == 0:
#         print(i)
#         # break


# 判断一个整数n是否是质数
# n = 8
# a = 2
# flag = 0
# while a < n:
#     if n % a == 0:
#         print(n, "不是质数")
#         flag = 1
#         break
#     a += 1
# # 只有当循环中的break未被执行过才会走到与while匹配的else中
# else:
#     print(n, "是质数")


n = 5
for i in range(2, n):
    if n % i == 0:
        print(n, "不是质数")
        break
else:
    print(n, "是质数")
