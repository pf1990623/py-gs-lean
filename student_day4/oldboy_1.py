data = [1, 2, 3]

for i in map(lambda x: x+1, data):
    print(i)

for index, i in enumerate(data):
    data[index] += 1
print(data)


"""
列表生成式
普通列表生成式
i+1 可以写三元运算
"""
data = [i+1 for i in data]
print(data)

data = [1, 2, 3, 4, 5, 6, 7, 8]
"""
列表生成式，套三元运算
"""
data = [i*2 if i > 5 else i for i in data]
print(data)

"""
一边循环一遍计算叫做 生成器
"""

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

"""
L 和 g 的区别就是，L为列表生成式，g则是生成器
"""

def fib(num):
    """
    :param num: 求多少个数列
    :return:
    """
    count = 0
    a, b = 0, 1
    while count < num:
        # a, b = b, a
        tpm = a
        a = b
        b = a + tpm
        count += 1
        # print(a)
        yield a
        """
        yield 作用：函数返回，同时挂起该函数
            b 返回给了通过__next__()调用当前函数的人
            这代表通过yield就实现了函数的中断，并且保存了函数的中间执行状态
        """
    print("...done")
f = fib(10000) #生成了一个生成器对象，集市代表推到公式准备好的意思
f.__next__()
f.__next__()
print(f.__next__())


"""
生成器实现的两种方法：
    1、采用列表生成式的方式用小括号括起来
    2、使用函数+yield方式
"""
"""
send 和__next__(),send可以传送数据，next只能唤醒 
"""

