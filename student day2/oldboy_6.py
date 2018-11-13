
#   6、使用for循环对s = "321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s = "321"
for i in s:
    print("倒计时%s秒" % i)
for i in s:
    print("倒计时{}秒".format(i))










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










#
# li = ['小粉嫩', '大铁锤']
# flag = True
# while flag:
#     inp = input('请输入内容:\n>>>').strip()
#     for i in li:
#         if inp.find(i) >= 0:
#             print('存在敏感字符,请重新输入')
#             break
#     else:
#         print(inp)
#         break








i = 0
sum = 0
while i < 99:
    i += 1
    if i == 88:  # 在当i=88的时候使88失效不继续运行，进而进行下一个循环
        continue
    elif i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
#






#   11、写代码：计算
#       1 - 2 + 3... + 99中除了88以外所有数的总和？
sum = 0
for i in range(0, 100):
    if i == 88:
        continue
    elif i % 2 == 0:
       sum -= i
       # print(sum)
    else:
        sum += i
        # print(sum)
print(sum)



# sum = 0
# count = 1
# while count < 100:
#     if  count %2 ==0:
#         sum -= count
#     else:
#         sum += count
#     count = count + 1
# print(sum)


# 练习题
# 用户输入一个数字
# 	判断是几位数？
# 	打印每一位数字级其重复的次数
# 	依次打印每一位数字，顺序个十百千万...位
#   输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印

m = input(">>>").split()
if len(m) == 5:
    pass
# are
# m = input(">>>").strip().lstrip("0")
# print("这是{}为数".format(len(m)))
#
# for i in range(len(m)):
#     print("{}'s count = {}".format(m[i],m.count(m[i])))
#
# for j in range(len(m)):
#     n = m[-j-1]
#     print(n)
# print(m)

while True:
    num = input(">>>>").strip()
    if num.isdigit():
        # num = int(num)
        break
    else:
        print("Bad number")

count = [0] * 10
print(count)
for i in range(10):
    count[i] = num.count(str(i))

for i in range(10):
    if count[i]:
        print(i, count[i])

lst = list(num)
lst.reverse()
print(lst)







#   31、av_catalog = {
#       "欧美": {
#           "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
#           "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
#           "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
#           "x-art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
#       },
#       "日韩": {
#           "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
#        },
#       "大陆": {
#           "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
#       }
#   }
#
#       a, 给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个元素：'量很大'。
#       b, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。
#       c, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收  费,屌丝请绕过"删除。
#       d, 将此["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]列表的"verygood"全部变成大写。
#       e, 给'大陆'对应的字典添加一个键值对'1048': ['一天就封了']
#       f, 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"]键值对。
#       g, 给此["全部免费,真好,好人一生平安", "服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'


av_catalog = {
      "欧美": {
          "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
          "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
          "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
          "x-art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
      },
      "日韩": {
          "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
       },
      "大陆": {
          "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
      }
  }
#a, 给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个元素：'量很大'。
av_catalog["欧美"]["www.youporn.com"].append("量很大")
print(av_catalog)
#       b, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。








# s = "⼩粉嫩⼤铁锤"
# while True:
#     i = input(">>>")
#     if i in s:
#         print("存在敏感字符请重新输⼊")
#         continue

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#           1)将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = "TT"
# print(lis)
lis[-3][-2][1][0]= "TT"
print(lis)
#           2)将列表中的数字3变成字符串"100"（用两种方式）。


#           3)将列表中的字符串"1"变成数字101（用两种方式）。
#
# from collections import namedtuple
# Point = namedtuple('xiaofeng', 'x y')
# p = Point(4, 5)
# print(p.x)
#
#
# # 居中显示，宽度30
# print("{:^30}".format('centered'))
# # 结果：           centered
# # 居中显示，宽度30，不够用*补全
# print("{:*^30}".format('centered'))
# # 结果：***********centered***********
# # 左对齐宽度2位
# print("{0}*{1}={2:<2}".format(2, 3, 2*3))
# # 结果2*3=6
# # 左对齐宽度2位，不够用0补齐
# print("{0}*{1}={2:<02}".format(2, 3, 2*3))
# # 结果：2*3=60
# # 左对齐宽度2位，不够用0补齐
# print("{0}*{1}={2:>02}".format(2, 3, 2*3))
# # 结果：2*3=06
# # print({"{0}*{1}={2:<2}".format(2,3,2*3))
# # print("{0}*{1}={2:<02}".format(3, 2, 6))
# # print('{0}*{1}={2:>02}'.format(3, 2, 6))
# #
#
# # 练习题
# # # 用户输入一个数字
# # # 	判断是几位数？
# # # 	打印每一位数字级其重复的次数
# # # 	依次打印每一位数字，顺序个十百千万...位
# # # 输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印
#
#
#
#
# print("=================")
#
# lst = ['1', '2', '3']
# print("\"".join(lst))
# print(" ".join(lst))
# print("\n".join(lst))
# lst = ['1', 'a', 'b', '3']
# print(" ".join(lst))
# s1 = "I'm \ta super student"
# s2 = s1.split('\t', 2)
# print(s2)
# s3 = s1.split()
# s1.rsplit()
# s1.lstrip()
#
# s = "I'm a super student"
# print(s.partition('s'))
# # ("I'm a ", 's', 'uper student')
# print(s.partition('uper'))
# # ("I'm a s", 'uper', ' student')
# print(s.rpartition('abd'))
# # ('', '', "I'm a super student")
# s = "hello world"
# print(s.title())
# # Hello World
# print(s.capitalize())
# # Hello world
# print(s.ljust(50, '#'))
# # hello world#######################################
# print(s.rjust(50, '#'))
# # #######################################hello world
# print(s.center(50))
#
# s = """I am very very very sorry    """
# print(s.strip('r y'))
# print(s.strip('r yamI'))
# s = "hello world"
# # print(s.index())
#
#
# # li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# # pl = []
# # while True:
# #     pinglun = input(">>输入评论内容(退出q)：")
# #     if pinglun == 'q':
# #         break
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# a = input('请输入评论:\n>>>').strip()
# b = []
# for i in li:
#     a1 = '*' * len(i)
#     if i in a:
#         a2 = a.replace(i, a1)
#         b.append(a2)
# print(b)