# 13、 写函数,接收两个数字参数,将较小的数字返回.
def fun13(x, y):
    minimum = min(x, y)
    return minimum
s = fun13(3, 6)
print(s)


def fun13_1(x, y):
    print(min(x,y))

fun13_1(3, 6)