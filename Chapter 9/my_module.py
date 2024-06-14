author = "mia"


def add(a, b):
    return a + b


def total(*args):
    # 参数args: 接收一个列表
    # return: a列表中每个元素的平方和
    result = 0
    for i in args:
        result += i**2
    return result


print(add(3, 4))
print(total(1, 2, 3, 4))
