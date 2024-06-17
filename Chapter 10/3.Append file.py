# 打开文件
f = open("./Chapter 10/test3.txt", mode="a", encoding="utf-8")

# 写入文件
f.write("Hello, World!\n")
list = ["a", "vb\n", "c\n"]
f.writelines(list)

# 关闭文件
f.close()
