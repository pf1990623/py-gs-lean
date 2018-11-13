#   8、升级题：实现一个整数加法计算器（多个数相加）：
#       如：content = input("请输入内容:")
#       用户输入：5 + 9 + 6 + 12 + 13，然后进行分割再进行计算。
s = input(">>>")
s = s.split('+')
sum = 0
for i in s:
    if not i:
        continue
    else:
        sum += i
print(sum)