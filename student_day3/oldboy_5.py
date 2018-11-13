# 5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为
#       {0:11,1:22,2:33}。

y = [11, 22, 33]
def fun5(lst):
    dic = {}
    if type(lst) is list:
        for i in range(len(lst)):
            dic[i] = lst[i]
        return dic
    else:
        pass
x = fun5(y)
print(x)

# lst = [1, 2, 3]
# if type(lst) is list:
#     print("cans is list")
# else:
#     print(" cans is not list")
