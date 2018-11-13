dic = {'name':'alex','age':18}
# 字典的特性：字典是无须的，列表是有序的。
# 字典的增删改查
# 查询

print(dic['name'])
print(dic['age'])  #使用【】如果key不存在，则返回报错

print(dic.get('name'))  #可以判断key是否存在，如果不存在返回none

# 增加 add
dic['gender'] = 'female'
print(dic)

# 修改
dic['name'] = 'zhangsan'
print(dic)

#del
del dic['name']
print(dic)

# 字典中key的定义规则
#1、不可变，判断一个key是否可变的：数字，字符串，元组
# 可变(列表)，检测方法hash()
# 元组：定义符号（），与列表万全一致，唯一不同的是元组内元素不可变
# key不可以重复
dic1 = {
    1:'alex',
    'name':'a',
    (1,2,3):{'age':18}
}

#value：定义任意类型
print(dic1.get((1,2,3)).get('age'))

# ---------------定义字典的其他方法
dic3=dict()
dic4=dict(name='zhangsan',age=19)
dic5=dict({'name':'zhangsan','age':19})
dic6=dict((('name','alex'),('age',18)))
print(dic6)

#--------字典的内置方法
dic = {'name':'alex','age':18}
# 清空
# dic.clear()
# print(dic)
# dic1=dict.fromkeys('hello','a')
# print(dic1)
# print(dic.items())
# for k,v in dic.items():
#     print(k,v)
# print(dic.keys())
# for i in dic.keys():
#     print(i,dic.get(i))
#
# #dic.pop('name')  #需要指定key,key必须存在，否则报错
# print(dic)
#
# # dic.popitem()    #随机删除一个项，即key:values
# print(dic)
# print("-----------------")
# # dic.setdefault('key1',[]).append(1)
# dic.setdefault('key1',[])
# dic['key1'].append(1)
#
# print(dic)
#
# # dic.update(dic1)
# # print(dic)
# dic.update(key1=23)
# print(dic)
# print(dic.values())


# 深copy和浅copy
# 字典中copy方法，浅拷贝即第一层的字典，第二层的字典还是共享的
# 深copy:完全复制，用新的内存地址
# import copy
# dic3 = copy.deepcopy(dic)
# print(dic3)
# #copy模块中的copy即浅拷贝
# # 作用：
# for key in dic3:
#     print(key,dic3[key])