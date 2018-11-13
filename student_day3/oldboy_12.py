# 12、 下面代码成立么?如果不成立为什么报错?怎么解决?
# 题目一：
# a = 2
# def wrapper():
#     print(a)
#
# wrapper()
# 函数是独立存在，不应该依赖外面的条件而存在，函数应该独立运行
# 不成立
# 题目二：
# a = 2
# def wrapper():
#     a = 2
#     a += 1
#     print(a)
# wrapper()
#
# # 定义方法是错误的
#
# # 题目三：
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()
# # 题目四：
# def wrapper():
#     a = 1
#     def inner():
#         a += 1
#         print(a)
#     inner()
# wrapper()

# 修改为
def wrapper():
    a = 1
    def inner(a):
        a += 1
        print(a)
    inner(2)
wrapper()