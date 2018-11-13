# def sayHi():
#     print("Hello i'm siri!")
#
# sayHi()
# sayHi()
# sayHi()
# sayHi()
#
# print(sayHi())
#
# def sayHi(name):
#     print("Hello i'm %s" % name)
#
# sayHi("alex")

# def sayHi(name, age, nationality="CN", sex = 'F'):  #name,age是形参,nationality="CN"形参的默认值,默认参数学到后边
#     # 位置参数，naem,age,没有赋值
#     # 默认参数 sex,nationality,
#     print("Hello i'm %s" % name, age, sex, nationality)
#
# sayHi("alex", 22, nationality="JP") # alex,22 实际参数,简称实参
# #   关键字参数，默认按顺序依次赋值，关键参数放在最右边

# 函数的参数
# 形参：  只有在被调用时，才分配内存单元，在调用是，即刻释放
# 实参：
# 默认值:
# 位置参数：
# 关键字参数：
# 非固定参数：*args       元祖形式
# 非固定参数：**kwargs   字典形式

# 局部变量和全局变量的访问顺序

# *args，默认是把每个实参当一个参数来返回，如果参数前面加*，则把参数打散，重新封装成元组

# **kwargs 函数执行时，实参不加*，则参数不会被打散
a = 'abc'
def funx(**kwargs):
    return kwargs

y = funx(abc=1,abcd=2)
print(y)








def grandpa():
    # x=1
    def dad():
        x = 2

        def son():
            x = 3
            print(x)

        son()

    dad()  # 嵌套函数的执行要求每一层级的函数都必须执行（调用），否则最外层不会执行最内层的函数


grandpa()

# 匿名函数
def calc(n):
    return n*n
print(calc(8))

# 匿名函数 lamba
calc2 = lambda x, y: x*y   # 第一个x为形参，x*x 相当于return返回值,不能跟默认参数
print(calc2(8, 8))

# map() 方法
# 把后面列表中的值交个前面函数去执行
def calc3(n):
    return n * n
data = map(calc3, range(10))
print(data)
for i in data:
    print(i)

# lanba()函数一般跟map() 函数结合
data = map(lambda n: n*2, range(10))
for i in data:
    print(i)
#
# 需求，如果n>5时，执行n * 2
data = map(lambda n: n*2 if n > 5 else n, range(10))
for i in data:
    print(i)

# 需求升级，小于5的都修改为负数
def cal5(n):
    return -n

data = map(lambda n: n*2 if n > 5 else cal5(n), range(10))

for i in data:
    print(i)

# 高阶函数
# 变量可以指向函数，函数的参数可以接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称为高阶函数

def fun111(x, y, f):
    return f(x) + f(y)

res = fun111(3, -6, abs)
print(res)

# 函数式编程
# 函数是python内建支持的一种封装，我们通过把大段的代码拆成函数，通过一层层的函数调用，就可以把复杂的任务分解成简单点的任务，这种
# 分解可以称之为面向过程的程序设计，函数就是面向过程的程序设计的基本单元
# 函数式变成中的函数术语并不是指计算机中的函数（实际上是Subroutine）,而是指数学中的函数，即自变量的映射，也就是说一个函数的值
# 仅决定于函数参数的值，不依赖其他状态，部署sqrt(x)函数，计算x的平方根，只要x不变，无论什么时候调用，调用多少次，值都是不变的的

# python对函数式变成提供部分支持，由于python允许使用变量，因此python不是纯函数式编程
# 简单说， 函数式编程是已成编程范式，也就是如何写程序的方法论，主要思想是把预算过程尽量写成一系列嵌套函数调用，

# 变成凡是
# 面向过程
# 棉线搞对象
# 函数式编程

