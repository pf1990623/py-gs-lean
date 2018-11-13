#   2、有字符串s = "123a4b5c"
#       1)通过对s切片形成新的字符串s1, s1 = "123"
s = "123a4b5c"
s1 = s[0:3]
print(s1)
#       2)通过对s切片形成新的字符串s2, s2 = "a4b"
s2 = s[3:6]
print(s2)
#       3)通过对s切片形成新的字符串s3, s3 = "1345"
s3 = s[0::2]
print(s3)
#       4)通过对s切片形成字符串s4, s4 = "2ab"
s4 = s[1:6:2]
print(s4)
#       5)通过对s切片形成字符串s5, s5 = "c"
s5 = s[-1]
print(s5)
#       6)通过对s切片形成字符串s6, s6 = "ba2"
s6 = s[-3::-2]
print(s6)


# coding=utf-8
# print("hello world")
#
# content = input(">>")
# content = content.split('+')
# print(content)
# sum = 0
# for i in content:
#     if not i:
#         continue
#     else:
#         sum += int(i)
# print(sum)
#
#
# s = '321'
# for i in range(len(s)):
#     print("倒计时%s秒"%(s[i]))
#
# s = '321'
# for i in s:
#     print('倒计时%s秒'%i)
# while True:
#     print("输入A or B or C")
#     chiose = input('>>>')
#     if chiose == 'A':
#         print("1.公交车，2.步行？")
#         chiose_A = input(">>>")
#         if chiose_A == 1:
#             print("10分钟到家")
#             break
#         else:
#             print("20分钟到家")
#             break
#     elif chiose =='B':
#         print("走小路回家")
#         break
#     elif chiose =='C':
#         print("1.游戏厅，2、网吧")
#         chiose_C = input(">>>")
#         if chiose_C== 1:
#             print("一个半小时到家，爸爸在家，拿棍等你")
#             continue
#         else:
#             print("两个小时到家，妈妈已做好了战斗准备。")
#             continue

from collections import namedtuple
Point = namedtuple('P','x,y')
print(type(Point))
p1 = Point(4,5)
print(p1)
print(p1.x,p1.y)
print(p1.x+p1.y)

# 练习，排序算法
# 依次接收用户数呼入的三个数，排序后打印
# 转换int,判断大小
# 使用max函数
# 使用列表sort方法
# 使用冒泡法
# a = input('>>>a')
# b = input(">>>b")
# c = input(">>>c")
# if a >= b >=c:
#     print(a,b,c)
# elif a >=c


num_list = [[1,9,8,5,6,7,4,3,2,],[1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
lenth = len(nums)
count_swap = 0
count = 0
for i in range(lenth):
    for j in range(lenth-i -1):
        count +=1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            count_swap +=1
print(nums,count_swap,count)

# 方法升级
flag = False
num_list = [[1,9,8,5,6,7,4,3,2,],[1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
lenth = len(nums)
count_swap = 0
count = 0
for i in range(lenth):
    for j in range(lenth -i -1):
        count+=1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums, count_swap, count)

# 再升级
# 方法升级

num_list = [[1,9,8,5,6,7,4,3,2,],[1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
lenth = len(nums)
count_swap = 0
count = 0
for i in range(lenth):
    flag = False
    for j in range(lenth -i -1):
        count+=1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums, count_swap, count)

# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))
# li.insert(0, "Tony")
# print(li)
# li[1] = "Kelly"
# print(li)
# l2 = [1, "a", 3, 4, "heart"]
# li = li + l2
# print(li)
# s = "qwert"
# s = list[s.]
# # li = li + s
# # print(li)
# li.pop(1)
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou",1]
# li.reverse()
# print(li)
#
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l1 = li[0:3]
# print(l1)
#
#
# l2 = li[3:6]
# print(l2)
# l3 = li[::2]
# print(l3)
# l4 = li[1:6:2]
# print(l4)
# l6 = li[-3::-2]
# print(l6)

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0] = "TT"
print(lis)
ls = []
# for i in range(3,50,3):
#     ls.append(i)
# print(ls)


# for i in range(1, 50):
#     if i % 3 == 0:
#         ls.append(i)
#     else:
#         continue
# print(ls)
# for i in range(100,0,-1):
#     print(i)




#
# st1 = "小粉嫩大铁锤"
# lst = ['小粉嫩','大铁锤']
# while True:
#     s = input(">>>")
#     if s in lst:
#         print("存在敏感字符请重新输")
#         continue
#     else:
#         break

# ls1 = []
# ls2 = []
# for i in range(100, 10, -2):
#     ls1.append(i)
# for j in ls1:
#     if j % 4 !=0:
#         continue
#     else:
#         ls2.append(j)
# print(ls2)

#   28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
#       敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
#       则将用户输入的内容中的敏感词汇替换成等长度的 *（苍老师就替换 ** *），
#       并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
#   27、查找列表li中的元素，移除每个元素的空格，并找出以
#       "A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中, 最后循环打印这个新列表。
#       li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# ls1 = []
# for i in li:
#     i = i.strip()
#     if (i.startswith('A') or i.startswith('a')) and i.endswith('c'):
#         ls1.append(i)
# for i in li:
#     if (i.strip().startswith('A') or i.strip().startswith('a')) and i.strip().endswith('c'):
#         ls1.append(i)
# for j in ls1:
#     print(j)
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# tu[1][2]['k2']="Seven"
# tu[1][2]['k3']="Seven"
# print(tu)
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for k,v in dic.items():
    print(k,v)
dic['k3'].insert(0,18)
print(dic)
a = "k:1|k1:2|k2:3|k3:4"
dic = dict(a.split('|'))
print(dic)