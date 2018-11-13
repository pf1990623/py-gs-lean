#   30、字典dic, dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
#       a.请循环输出所有的key
for i in dic:
    print(i)
#       b.请循环输出所有的value
for i in dic:
    print(dic[i])
#       c.请循环输出所有的key和value
for k,v in dic.items():
    print(k,v)
#       d.请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典'
dic['k4'] = 'v4'
print(dic)
#       e.请在修改字典中"k1"对应的值为"alex"，输出修改后的字典
dic['k1'] = 'alex'
print(dic)
#       f.请在k3对应的值中追加一个元素44，输出修改后的字典
dic['k3'].append(44)
print(dic)
#       g.请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
dic['k3'].insert(0,18)
print(dic)