#   24、利用for循环和range
#       找出50以内能被3整除的数，并将这些数插入到一个新列表中。
ls = []
for i in range(3,50,3):
    ls.append(i)
print(ls)
for i in range(1, 50):
    if i % 3 == 0:
        ls.append(i)
    else:
        continue
print(ls)