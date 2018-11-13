# abs(1)  # 绝对值
# all('a')  # 判断一个序列是中有一个值为假其他是真，也是假，类似于and
# any('a')  # 判断一个序列中有一个值为真，则返回真  类似或
# ascii('a')  # 用不到
# bin()      # 二进制
# bool()  # 判断是否是true
# bytes()  # 不可修改
# bytearray()  # 可变的bytes
# callable('a')  # 判断一个对象是否可以调用
# chr(97) # ascii 码 数字对应 字符
# ord('b') # 将assic 中的而数字
# classmethod()  # 面向对象使用
# compile()    #
# complex()    # 复数
# eval()   # 执行简单的计算，不能进行赋值
# exec()   #
# dict()
# dir()  # 返回
# divmod(10, 2)   # 返回商，余数
# filter(lambda x: x>5,range(10))   # 返回满足条件的值
# frozenset({1, 2, 3, 3, 5})   # 将一个集合变为只读
# globals()   # 当前程序开辟的所有空间都以字典的形式打印出来，只显示全局变量
# locals()    # 只打印局部变量
# hash()      # 判断是否可hash
# help()       # 帮助手册
# hex()        # 10进制转16进制
# max(3, 6)    # 返回最大值
# min(3, 6)   # 求最小值
# next()      #
# object()
# oct()     #
# pow(4, 9)     # 4的9次方
# oct(8)     # 八进制
# open()    # 打开文件
# print()  # print可以往文件输入
# # ####print 写入到文件中
msg = "ancd"
f = open("tofile", 'w', encoding='utf-8')
print(msg, sep='|', end='', file=f)
#################################
# range()  # 返回一个序列
# repr()   # 返回一个字符串格式
# reversed()
data = list(range(10))
date = reversed(data)
print(data)
print(round(2.6))  # 整数是奇数，4舍五入， 如果是双数，5舍6入


# 列表转集合
data = [2, 3, 3, 5]
a = set(data)
print()
# #######
a = 'abc'
print(sorted(a))
# zip()  #
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8]
for i in zip(a, b):
    print(i)




