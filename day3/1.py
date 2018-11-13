# 练习题
# 打印一个边长为N的正方向
# n = int(input(">>>"))
# print(n*'*')
# for i in range(n-2):
#     print("*", ''*(i-1), '*')
# print(n*'*')
# for i in range(4)
# 求100内所有奇数的和（2500）
# n = 0
# for i in range(1, 100, 2):
#     n += i
# print(n)
# 判断学生成绩，成绩等级A-E。其中90分以上为A，８０－８９分为B，７０－７９为C　６０－６９为D，６０为E
# store = int(input("store"))
# if store > 90:
#     print("A")
# elif 80 <= store <=89:
#     print("B")
# elif 70 <= store <=79:
#     print("C")
# elif 60 <= store <=69:
#     print("D")
# else:
#     print("E")


# 求1-5阶乘之和
# sum = 0
# # n = 1
# # for i in range(1, 6):
# #     print('%s = %s * %s' %((n*i), n, i))
# #     n *= i
# # print(n)
# # print(sum)

# 给一个数，判断是否是素数（质数）
#   质数：大于1的自然数只能被1和他本身整除
# n = int(input(">>>"))
# for i in range(2, n):
#     if n % i == 0:
#         print(" is not a prime number")
#         break
# else:
#     print("is a prime number")
# n = 12577
# flag = False
# for i in range(2, n+1):
#     if n % i == 0: # 找到条件
#         flag = True
#         print(i)
#         break
# if flag:
#     print(n, "is not a prime number")
# else:
#     print(n, "is a prime number")


# 开方
# n = 126557
# for i in range(2, int(n**0.5)+1):
#     if n % i == 0:
#
#             break
# else:
#     print("is a prime number")



# 打印99乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j > i:
#             print("\n")
#             break
#         print(j, "*", i, "=", i*j, end=' ')

# # 打印菱形
# print("*"*3)
# count = 1
# for i in range(-3, 4, 1):
#     print(' ' * i, '*'*count, ' ' * i)
#     count += 1
#     if i > 0:
#         print('*'*7)
#         count -=1

# 打印100以内裴波纳契数列
# x = 0
# y = 1
# count = 1
# while count > 0:
#     z = x + y
#     x = y
#     y = z
#     if z > 100:
#         break
#     count += 1
#     print(z)

# 求裴波纳契数列第101项
# x = 0
# y = 1
# count = 1
# while count > 0:
#     z = x + y
#     x = y
#     y = z
#     count += 1
#     if count > 101:
#         break
# print(z)
# 求10W内所有的素数
# for i in range(2, 50):
#     for j in range(2, 50):
#         if i % j != 0:
#             print(i, "是质数")
#             continue
#         else:
#             print(i, "不是质数")
#             continue

# 打印正方形
# n = input(">>>")
# n_num = len(n)
# n = int(n)
# print("*"*n)
# for i in range((n-2)):
#     print("*", ""*(n-2), "*")
# print("*"*n)

# 给定一个5位数，判断该数的位数，依次打印出个位，十位，百位，千位，万位的数字
# c = input(">>>")
# n = len(c)
# c = int(c)
# w = 10000
# for i in range(1, (n+1)):
#     print(c // w)
#     c %= w
#     w //= 10

# 练习题
# 给一个半径，求圆的面积和周长。圆周率3.14
# n = int(input(">>>"))
# print('area='+str(3.14 * r * 4))
# print("circumference"+ str(2*3.14 * r))
# # 输出两个数，比较大小，从小到大升序
# x = int(input("x="))
# y = int(input("y="))
#
# if x > y:
#     print(x, y)
# else:
#     print(y, x)

# 三元运算符，三木运算符
# 三元表达式
# 真值 if 条件 else 假值
# x = int(input("x="))
# y = int(input("y="))
# print(x, y) if x > y else print(y, x)
# 获取最大值，请输入若干个整数，打印出最大值
# max = 0
# count = 0
# while True:
#     num = int(input(">>>"))
#     if num  > max:
#         max = num
#     count +=1
#     if count > 2:
#         choice = input("continue?(Y/N):")
#         if choice == 'N':
#             print(max)
#             break
# print(5 / 1)
# 输入N个数，求每次输入后的算数平均值
# count = 0
# sum = 0
# while True:
#     num = int(input(">>>"))
#     sum += num
#     count += 1
#     print(sum / count)
# print('*'*7)
# count = 1
# for i in range(-3, 4):
#     # print(i)
#     print(' '*i, '*'*(7+i*2), ' ' * i)
#     # if i == 0:
#     #     continue
#     # else:
#     #     print(' '*i, '*'*(7-i*2), ' ' * i)
# print('*'*7)

# 打印菱形
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# for i in range(-3, 4):
#     if i > 0:
#         print(' ' * i, '*' * (7 - i * 2))
#     else:
#         print(' '*(-i), '*'* (7 + i * 2))
# for i in range(-3,4):
#     print(' ' * i, '*' * (7 - i * 2)) if i > 0 else print(' '*(-i), '*'* (7 + i * 2))
# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%sx%s=%s" % (j, i, j*i), end="\t")
#     print()
# print()函数，sep= ''代表分隔符，end='',默认end = '\n' 换行

# print("{0}{1}{2}".format(1, 2, 3))
# # 右对齐
# print('a={:20}'.format(12))
# # 左对齐
# print('a={:<20}'.format(12))
# # 右对齐
# print('a={:>20}'.format(12))
# # 格式化输出 {:<2} :<2冒号是分隔符,<表示左对齐，2表示宽度
# 扩展题
# for i in range(1, 10):
#     for j in range(i, 10):
#         if i >= j:
#             print()
#             print(str('\t\t'*(i-1)), end="")
#         print("{}x{}={}".format(i, j, i*j), end="\t")
# for i in range(-3,4):
#     print(" "*abs(i)+"*"*(7-2*abs(i)))
