# import my_module
# from my_module import add, author, total
# from my_module import *
from my_module import add as f  # 将导入的add方法重命名为f

result = f(3, 4)
print(result)
# print(author)
# total(1, 2, 3, 4)
