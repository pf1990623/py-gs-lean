lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(9):
    for j in range(8 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)

# for i in range(9):
#     for j in range(8, 0, -1):
#         if lst[j] > lst[j - 1]:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]
# print(lst)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# count = 0
for i, row in enumerate(matrix):
    print(i, row)
    for j, col in enumerate(row):
        print(j, col)
        if i < j:
            # tmp = matrix[i][j]
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
            # matrix[j][i] = tmp
            # count += 1
print(matrix)

# 任意矩阵，求其转换矩阵


# print(count)
# 练习题
# 用户输入一个数字
# 	判断是几位数？
# 	打印每一位数字级其重复的次数
# 	依次打印每一位数字，顺序个十百千万...位
# 输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印

# num = input(">>>")
# # num = str(num)
# print(num.count('1'))

num = input(">>>").strip()
for i in range(10):
    if num.count(str(i)) == 0:
        continue
    print(i, num.count(str(i)))

for i in range(len(num)+1):
    if i == 0:
        continue
    print(num[-i])

# print(len(num))

# 有一个方阵
# 1 2 3            1 4 7
# 4 5 6   ===》    2 5 8
# 7 8 9            3 6 9


# while True:
#     num = input(">>>").strip()
#     # num = str(num)
#     for i in range(10):
#         if num.count(str(i)) == 0:
#             continue
#         print(i, num.count(str(i)))