"""
*
***
*****
*******

((n*2-1)-1)/2 = n-1

i=0 b=n-1 a=1
i=1 b=n-2 a=3
i=2 b=n-3 a=5
"""

# 打印n行等腰三角形
n = 7
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (i * 2 + 1))


# 穷举
peach = 1
while True:
    d1 = peach // 2 - 1
    d2 = d1 // 2 - 1
    d3 = d2 // 2 - 1

    if d3 == 1:
        print(peach)
        break
    peach += 1
