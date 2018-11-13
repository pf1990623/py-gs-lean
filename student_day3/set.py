# 集合
# s1 = {'a', 1, 2, 3, 3, 3}
# s2 = {'b', 1, 3, 5, 7, 9.3}
# # 打印类型
# print(type(s1))
#
# # 交集
# print(s1 & s2)    #intersection 交集
# print(s1.intersection(s2))
#
# # 并集
# print(s1|s2)     #union  并集
# print(s1.union(s2))
#
# # 差集
# print(s1-s2)   # 减掉公有的部分
# print(s2-s1)
# print(s1.difference(s2))
#
# # 对称差集 ：去掉共有的部分，剩余的所有
# # print(s1 ^ s2)
# # print(s1.symmetric_difference(s2))
#
# # 子级
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3}

# print(s2 >= s1)
# print(s1.issubset(s2))



# # 父级
# print(s1.issuperset(s2))
# print(s1 >= s2)

#其他内置方法
# add（）方法 添加的是一个整体
s1.add("hello")
print(s1)

# 集合更新，updata方法跟的是一个 可迭代的对象
s1.update('hello')
print(s1)

# 随机删除
s1.pop()
print(s1)

# 删除,如果删除对象不存在，就会报错
s1.remove(2)
print(s1)

# 使用remove()方法,删除不存在的对象不存在，使用discard（）则不会报错
s1.discard('n')
print(s1)

s1.difference_update(s2)
print(s1)