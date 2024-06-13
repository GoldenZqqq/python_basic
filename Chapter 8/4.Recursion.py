# 上台阶
# 10阶楼梯，每次上1个台阶或者2个台阶，问一共有多少种走法
# f(n) = f(n-1) + f(n-2)
# n = 0, f(n) = 0
# n = 1, f(n) = 1
# n = 2, f(n) = 2
def climbStairs(n):  # 计算出走n阶台阶，一共有多少种走法
    if n == 0 or n == 1 or n == 2:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)


print("楼梯有%d阶的时候，有%d种走法" % (5, climbStairs(5)))

a = [0, 1, 2]
for i in range(3, 11):
    a.append(a[i - 1] + a[i - 2])
    print("楼梯有%d阶的时候，有%d种走法" % (i, a[-1]))
