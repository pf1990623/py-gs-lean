# 5的阶乘
n = 1
for i in range(1, 6):
     n *= i
print(n)


# 1-5的阶乘之和
n = 1
sumn = 0
for i in range(1, 6):
    n *= i  # n = n * i
    sumn += n
print(sumn)