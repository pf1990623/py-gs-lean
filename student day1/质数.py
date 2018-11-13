# 输入一个数，判断该数是否是质数
n = int(input(">>>"))
for i in range(2, n):
    if n % i == 0:
        print("不是质数")
        break
else:
    print("质数")

# 方法升级
n = int(input(">>>"))
for i in range(2, int(n ** 0.5 + 1)):
    if n % i == 0:
        print("不是质数")
        break
else:
    print("质数")

# 方法再升级
count = 1
import datetime
start = datetime.datetime.now()

for x in range(3, 100000, 2):
    if x > 10 and x % 10 == 5:  # 为什么
        continue
    for i in range(3, int(x ** 0.5)+1, 2): # 为什么从三开始，sep 为2，因为已经是奇数，除2没有意义
        if x % i == 0:
            break
    else:
        count += 1
        # print(x,count)
        # print(x)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)

# 再升级
start = datetime.datetime.now()
number = 100000
count = 2
for num in range(4, number):
    if num % 6 != 1 and num % 6 != 5:
        continue
    else:
        # snum = int(num**0.5+1)
        for i in range(5, int(num**0.5+1), 2):
            if not num % i:
                break
        else:
            count += 1
            # print(num)
            pass
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
