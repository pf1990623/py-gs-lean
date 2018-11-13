# 14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
#   例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
#
# s = ['1', '老男孩', '武sir']
# xy = "_".join(s)
# print(xy)




from collections import Iterable
def fun14(*args):
    ls = []
    if isinstance(args, Iterable):
        for i in args:
            if type(i) == int:
                i = str(i)
            ls.append(i)
        return '_'.join(ls)
    else:
        print("参数非可迭代对象")

z = fun14(*[1,'老男孩','武sir'])
print(z)

