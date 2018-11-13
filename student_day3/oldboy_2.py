# 2、 传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
# def fun2(x):
#     print(len(x))
#
# fun2()

def check_str(msg):
    res={
        'num': 0,
        'string': 0,
        'space': 0,
        'other': 0,
    }
    for s in msg:
        if s.isdigit():
            res['num'] += 1
        elif s.isalpha():
            res['string'] += 1
        elif s.isspace():
            res['space'] += 1
        else:
            res['other'] += 1
    return res

res=check_str('hello name:aSB passowrd:alex3714')
print(res)
