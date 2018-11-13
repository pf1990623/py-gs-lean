#变量：用来记录状态
#变量值的变化即状态的变化：程序运行的本质就是处理一系列状态的变化
#python的五大基本数据类型：
# 数字、字符串、列表、元组、字典
# 1、数字
#  python中的数字类型又分为：整型、长整型、浮点数
# oct():十进制转八进制函数
# hex():十进制转16禁止函数
# 整型的内置函数int()
# int()
# int(x, base=10) -> integer  base=10代表x为10进制的整数
# bin():10进制转2禁止函数
print(bin(10))   # 10转换转2禁止
print(oct(10))   # 10转换8禁止
print(hex(10))   # 10转换为16禁止

print(int('1010',base=2))
print(int('012',base=8))
print(int('0xa',base=16))
# python中没有长整型，python2中有长整型
# type()函数，判定数据类型
# bool类型：值为0和1，即true 或者false
# float类型: 简单类型为小数
# complex类型：复数，
# 小结：数字类型：整型、长整型、布尔、浮点、复数
# 字符串
# 定义：单引号或者双引号或者三引号包含的值
# 字符串内置方法
a = 123
print('aaa',a)

print ()
