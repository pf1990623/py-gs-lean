# 打印倒菱形
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
n = 7
e = n//2
for i in range(-e, n-e):
    if i < 0:
        prespace = -i
    else:
        prespace = i
    print(' '*(e-prespace) + '*'*(2*prespace+1))
# # 升级方法
n = 7
e = n//2
for i in range(-e, n-e):
    print(' '*(e-abs(i)) + '*'*(2*abs(i)+1))

# 打印菱形
for i in range(-3, 4):
    if i < 0:
        print(' ' * (-i)+'*' * (i + 4))
    elif i > 0:
        print(' '*3 + '*'*(4-i))
    else:
        print('*'*7)
