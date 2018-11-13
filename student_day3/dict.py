ls = [1, 2, 3]
for j in range(len(ls)):
    j = ls[j]
    print(j)







dic = {'name': 'alex', 'age': 18}
# 字典的内置方法
dic.clear()  # 字典清空
dic.copy()  # 浅拷贝操作
# 快速生成要给字典，可以是字符串，也可以是一个列表，seq
# dic1 = dict.fromkeys('hellp',1)
# print(dic1)
# print(dic1.items())  # 将字典更改为一个列表套元祖的方式
dic = {'name': 'alex', 'age': 18}

for k, v in dic.items():
    print(k, v)

print(dic.keys())

for i in dic.keys():
    print(i, dic.get(i))

# dic.pop('age')   # key必须存在，否则报错
print(dic)
print(dic.popitem())  # 随机删除

print(dic.values())




# # 字典的常用方法
# dic = {'name': 'alex', 'age': 18}
# # 增
# dic['k1'] = 'xiaofeng'
# print(dic)
# # 删
# del dic['age']
# print(dic)
# # 改
# dic['name'] = 'panfeng'
# print(dic)
# # 查询
#
# print(dic['name'])   # 如果key不存在，报错
# print(dic.get('name'))  # 如果key不存在，返回None

# 字典key的定义规则
# 1、不可变，数字、字符串、元祖是不可变的，即不可hash()
#     列表是可变的
# 2、key是不可以重复的，唯一的
# value定义规则
#  value可以是任何值
# 字典的定义方法
