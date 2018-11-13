"""
迭代器：
    列表，字典，字符串是一个可迭代的对象，列表、字典、字符串转为迭代器 使用iter()方法
判断一个变量是否是可迭代对象
生成器也是可迭代对象

可以被next()函数调用的，并不断返回下一个值的的对象，被称为迭代器

isinstance()

所有的生成器都是迭代器，
多有的迭代器不一定都是生成器
如果使用iter()方法，一个是迭代器，一个是生成器


iterator 甚至可以表示一个无限大的数据流，例如全体自然数，而list是永远不可能存储所有的自然数

小结：
    凡是可以作用于for循环的对象都是Iterablel类型；
    凡是可作用于next()函数的对象都是iterator类型，它们表示一个惰性计算的序列
    结合数据类型如list、dict、str等是Iterable但不是Iterator，不过是通过iter()函数或得一个
    Iterator对象

    python的for循环本质就是通过不断调取Next()函数实现的

    range(10) 就是一个迭代器


"""
from collections import Iterable
a = [1, 2, 3]
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))

print(iter(a))
for i in range(10):
    pass

