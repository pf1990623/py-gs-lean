# 15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
#   例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)

def fun15(*args):
    max_number = max(args)
    min_number = min(args)
    # print(min_number)
    # print(max_number)
    dic = {
        "max": max_number,
        "min": min_number
     }
    return dic
x = fun15(2, 5, 7, 8, 4)
print(x)
