# 10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面.
#   例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)

a = [1, 2, 3]
b = (22, 33)
# s = tuple(a)
# print(s)
def fun10(x, y, *args):
    args = tuple(x) + tuple(y)
    return args
s = fun10(a, b)
print(s)


def fun11(*args):
    return args

s = fun11(*a,*b)
print(s)