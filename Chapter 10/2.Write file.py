# 打开文件
f = open("./Chapter 10/test2.txt", mode="w", encoding="utf-8")

# 写入文件内容
f.write("Hello, World!\n")
f.write("Who are you?\n")
context = ["Hello, World!", "Who are you?"]
for i in context:
    f.write(i + "\n")

# 关闭文件
f.close()


f = open("./Chapter 10/test2.txt", encoding="utf-8")  # 相对路径
context = f.read()
print(context)
f.close()
