#   18、写代码，有如下列表，按照要求实现每一个功能
#       li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#       1)计算列表的长度并输出
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(len(li))
#       2)列表中追加元素"seven", 并输出添加后的列表
li.append("seven")
print(li)
#       3)请在列表的第1个位置插入元素"Tony", 并输出添加后的列表
li.insert(0, "Tony")
print(li)
#       4)请修改列表第2个位置的元素为"Kelly", 并输出修改后的列表
li[1] = "Kelly"
print(li)
#       5)请将列表l2 = [1, "a", 3, 4, "heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加
l2 = [1, "a", 3, 4, "heart"]
li = li + l2
print(li)
#       6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
#       7)请给列表添加元素"eric", 并输出添加后的列表
li.append("eric")
print(li)
#       8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
li.pop(1)
print(li)
#       9)请删除列表中的第2至4个元素，并输出删除元素后的列表
del(li[2:4])
print(li)
#       10)请将列表所有得元素反转，并输出反转后的列表
li.reverse()
print(li)
#       11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
print(li.count("alex"))