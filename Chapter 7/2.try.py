try:
    print("有可能出现异常的代码")
    n = int(input("请输入一个数字："))
    n = 5 / n
    print("结果：", n)
except ZeroDivisionError as e:
    print("除数不能为0")
    print("原始报错信息", e)
except ValueError:
    print("输入的不是数字")
else:
    print("运行没有被except语句捕获，执行else模块")
finally:
    print("无论如何都要执行finally模块")
