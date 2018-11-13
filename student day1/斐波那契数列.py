# 求100 以内的斐波那契数列
# a = 0
# b = 1
# print(a, b, sep="\n")
# while True:
#     z = a + b
#     a = b
#     b = z
#     if z > 100:
#         break
#     print(z)

# 打印100以内裴波纳契数列
# x = 0
# y = 1
# print(x, y, sep='\n')
# while True:
#     c = x + y
#     x = y
#     y = c
#     if c > 100:
#         break
#     print(c)
# 斐波那契数列第101项
x = 0
y = 1
count = 3
while True:
    c = x + y
    x = y
    y = c
    if count > 101:
        break
    count += 1
print(c)
# for循环方法
x = 0
y = 1
for i in range(2, 102):
    c = x + y
    x = y
    y = c
print(c)

# 方法
x = 0
y = 1
count = 2
while True:
    z = x + y
    x = y
    y = z
    if count == 101:
        break
    count += 1
print(z)

# 方法
x = 1
y = 1
for i in range(2, 101):
    if i == 100:
        print(x+y)
    y += x
    x = y - x
