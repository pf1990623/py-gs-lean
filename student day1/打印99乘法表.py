# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%sx%s=%s" % (j, i, j*i), end="\t")
#     print()
# 99乘法表变异
# for i in range(1, 10):
#     for j in range(i, 10):
#         if i == j:
#             print()
#             print(str('\t\t'*(i-1)), end="")
#         print("{}x{}={}".format(i, j, i*j), end="\t")

# 99乘法再变异
# for i in range(1, 10):
#     for j in range(i, 10):
#         if i == j:
#             print()
#         print("{}x{}={}".format(i, j, i*j), end="\t")

# 99乘法表右对齐
# for i in range(1, 10):
#     for j in range(i, 10):
#         if i == j:
#             print()
#         print("{}x{}={}".format(i, j, i * j), end="\t")
# 99乘法表
for i in range(1, 10):
    s = ""
    for j in range(i, 10):
        s += "{}*{}={:<3} ".format(i, j, i*j)
    print("{:>80}".format(s))

for i in range(1, 10):
    s = " "
    for j in range(i, 10):
        s += "{}*{}={:<{}}".format(i, j, i*j, 2 if j < 4 else 3)
    print("{:>80}".format(s))
