s1 = "hello world"

# 序列的通用操作
print(s1 + "mia")
print(s1 * 3)
print(len(s1))
print(max(s1), min(s1))
print(ord("w"))
print(ord(" "))
# del s1
# print(s1)
print("s" in s1)
print("abcd" < "abce")
print("cd" < "abcd")

# 字符串的遍历
print("--------------- 字符串的遍历 ---------------")
for i in s1:
    print(i)
for index, value in enumerate(s1):
    print(index, value)
for i in range(len(s1)):
    print(i, s1[i])

# 类型转换
print("--------------- 字符串的类型转换 ---------------")
print(str(12), type(str(12)))  # int --> str
print(str([1, 2, 3, 4]), type(str([1, 2, 3, 4])))  # list --> str
print(str((1,)), type(str((1,))))  # tup;e --> str

# 常用方法
print("--------------- 字符串的常用方法 ---------------")
print(s1)
print(s1.islower())
print(s1.isupper())
print(s1.count("o"))
print(s1.strip())  # 删除首尾空格
print(s1.split(" "))  # 分隔字符串
print(s1.find("a"))
print("#$".join(["111", "222", "333"]))

# 字符串的统计
print("--------------- 字符串的统计 ---------------")
s = input("请输入一篇文章：")
# 字母的个数、数字的个数、符号的个数
a, b, c = 0, 0, 0
for i in s:
    if i.isdigit():
        b += 1
    elif i.isalpha():
        a += 1
    else:
        c += 1
print(a, b, c)
