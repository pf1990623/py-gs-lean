# 16、 写函数，传入一个参数n，返回n的阶乘
#   例如:cal(7) 计算7*6*5*4*3*2*1

def jc(n):
    count = 1
    for i in range(n, 0, -1):
        count *= i
    return count
print(jc(10))

def func16(a):
    count = 1
    for i in range(a, 0, -1):
        count *= i
    return count
print(func16(7))