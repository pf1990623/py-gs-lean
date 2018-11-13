#   7、实现一个整数加法计算器(两个数相加)：
#       如：content = input("请输入内容:")
#       用户输入：5 + 9
#       或5 + 9
#       或5 + 9，然后进行分割再进行计算。
s = input(">>>")
s = s.split('+')
sum = 0
for i in s:
    sum += i
print(sum)