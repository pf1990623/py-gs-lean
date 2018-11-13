# 输入N个数，求每次输入后的算数平均值
count = 0
sum = 0
while True:
    num = int(input(">>>"))
    sum += num
    count += 1
    print(sum / count)