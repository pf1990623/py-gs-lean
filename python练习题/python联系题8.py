# 输出 9*9 乘法口诀表
#分行与列考虑，共9行9列，i控制行，j控制列。
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" %(i,j,i*j),end=' ')
    print()
    #     print("%d*%d=%d" % (i, j, i * j))
    # print("\t")
# for i in range(1, 10):

#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j))

# 再升级就是每行依次递增打印


for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()