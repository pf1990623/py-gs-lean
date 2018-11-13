#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# -*- coding: UTF-8 -*-
#程序分析：可填写在百位、十位和个位的数字分别是1，2，3，4组成所有的排列后，再去掉不满足条件的序列
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i != k ) and ( i!= j) and ( k != j):
#                 print(i,j,k)

from itertools import permutations
for i in permutations([1,2,3,4],3):
    print(i)