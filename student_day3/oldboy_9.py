# 9、 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
#       a=10
#       b=20
#       def test5(a,b):
#           a=3
#           b=5
#       print(a,b)
#           c = test5(b,a)
#       print(c)


a = 10
b = 20
def test5(a, b):
    a = 3
    b = 5
    print(a, b)

c = test5(b, a)

print(c)

# a = 10
# b = 20
# c = None，因为test函数没有返回值，如果函数没定义返回值，默认返回None
