# 17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
#   例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

def fun17():
    l1 = ['红心', '黑桃', '梅花', '方块']
    str_class = list(range(2, 11))
    str_class.append('A')
    str_class.append('J')
    str_class.append('Q')
    str_class.append('K')
    l3 = []
    tmp = []
    for i in l1:
        for j in str_class:
            l3.append('(' + i + ',' + str(j)+ ')')
            # print(l3)

    return l3
x = fun17()
print(x)

# class_p = ['红心', '黑桃', '梅花', '方块']
# str_class = list(range(2, 11))
# str_class.append('A')
# str_class.append('J')
# str_class.append('Q')
# str_class.append('K')
# print(str_class)
# l3 = []

# for i in class_p:
#     for j in str_class:
#         stra = i + ',' + str(j)
#         l3.append(stra)
#     tup3 = tuple(l3)
# print(tup3)