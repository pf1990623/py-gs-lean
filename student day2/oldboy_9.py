#   9、计算用户输入的内容中有几个整数（以个位数为单位）。
#       如：content = input("请输入内容：")  # 如fhdal234slfh98769fjdla
s = input(">>>")
count = 0
for i in s:
    if i.isdigit() :
        count +=1
    else:
        continue