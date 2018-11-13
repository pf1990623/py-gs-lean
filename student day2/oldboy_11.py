#   11、写代码：计算
# #       1 - 2 + 3... + 99中除了88以外所有数的总和？
sum = 0
count = 0
while count < 99:
    count += 1
    if count == 88:
        continue
    if count % 2 == 0:
        sum -= count
    else:
        sum += count
print(sum)

sum = 0
for i in range(1, 100):
    if i == 88:
        continue
    elif i % 2 != 0:
        sum += i
    else:
        sum -= i
print(sum)