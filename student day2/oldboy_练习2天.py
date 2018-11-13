# 练习题：
name = " aleX leNb "
#   1、有变量name = "aleX leNb"
#       完成如下操作：
#       1)  移除name变量对应的值两边的空格, 并输出处理结果
print(name.strip())
#       2)  移除name变量左边的"al"并输出处理结果
print(name.lstrip('al'))
#       3)  移除name变量右面的"Nb", 并输出处理结果
print(name.rstrip('Nb'))
#       4)  移除name变量开头的a"与最后的"b",并输出处理结果
print(name.rstrip('b').lstrip('a'))
#       5)  判断name变量是否以"al"开头, 并输出结果
print(name.startswith('al'))
#       6)  判断name变量是否以"Nb"结尾, 并输出结果
print(name.endswith('Nb'))
#       7)  将name变量对应的值中的所有的"l"替换为"p", 并输出结果
print(name.replace('l', 'p'))
#       8)  将name变量对应的值中的第一个"l"替换成"p", 并输出结果
print(name.replace('l', 'p', 1))
#       9)  将name变量对应的值根据所有的"l"分割, 并输出结果。
print(name.split('l'))
#       10) 将name变量对应的值根据第一个"l"分割, 并输出结果。
print(name.split('l', 1))
#       11) 将name变量对应的值变大写, 并输出结果
print(name.upper())
#       12) 将name变量对应的值变小写, 并输出结果
print(name.lower())
#       13) 将name变量对应的值首字母"a"大写, 并输出结果
print(name.capitalize())
#       14) 判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count('l'))
#       15) 如果判断name变量对应的值前四位"l"出现几次, 并输出结果
print(name.count('l', 0, 5))
#       16) 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
print(name.index("N"))
#       17) 从name变量对应的值中找到"N"对应的索引(如果找不到则返回 - 1)输出结果】
print(name.find("N"))
#       18) 从name变量对应的值中找到"X le"对应的索引, 并输出结果
print(name.find("X le"))
#       19) 请输出name变量对应的值的第2个字符?
print(name[0:2])
#       20) 请输出name变量对应的值的前3个字符?
print(name[0:3])
#       21) 请输出name变量对应的值的后2个字符?
print(name[-3:-1])
#       22) 请输出name变量对应的值中"e"所在索引位置?
print(name.find("e"))
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
#   3、使用while或for循环分别打印字符串s = "asdfer"中每个元素。
s = "asdfer"
for i in s:
    print(i)
#   4、使用for循环对s = "asdfer"进行循环，但是每次打印的内容都是"asdfer"。
s = "asdfer"
for i in s:
    print(s)
#   5、使用for循环对s = "abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb, ...gsb。
s = "abcdefg"
for i in s:
    print(i+'sb')
#   6、使用for循环对s = "321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s = "321"
for i in s:
    print("倒计时%s秒" % i)
for i in s:
    print("倒计时{}秒".format(i))

#   7、实现一个整数加法计算器(两个数相加)：
#       如：content = input("请输入内容:")
#       用户输入：5 + 9
#       或5 + 9
#       或5 + 9，然后进行分割再进行计算。
s = input(">>>")
s = s.split('+')
sum = 0
for i in s:
    sum += i
print(sum)
#   8、升级题：实现一个整数加法计算器（多个数相加）：
#       如：content = input("请输入内容:")
#       用户输入：5 + 9 + 6 + 12 + 13，然后进行分割再进行计算。
s = input(">>>")
s = s.split('+')
sum = 0
for i in s:
    if not i:
        continue
    else:
        sum += i
print(sum)
#   9、计算用户输入的内容中有几个整数（以个位数为单位）。
#       如：content = input("请输入内容：")  # 如fhdal234slfh98769fjdla
s = input(">>>")
count = 0
for i in s:
    if i.isdigit() :
        count +=1
    else:
        continue


#   10、写代码，完成下列需求：
#       用户可持续输入（用while循环），用户使用的情况：
#       输入A，则显示走大路回家，然后在让用户进一步选择：
#           是选择公交车，还是步行？
#           选择公交车，显示10分钟到家，并退出整个程序。
#           选择步行，显示20分钟到家，并退出整个程序。
#       输入B，则显示走小路回家，并退出整个程序。
#       输入C，则显示绕道回家，然后在让用户进一步选择：
#           是选择游戏厅玩会，还是网吧？
#           选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B, C选项。
#           选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B, C选项。

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
#     elif chiose == 'B':
#         print("走小路回家")
#         break
#     elif chiose == 'C':
#         print("1.游戏厅，2、网吧")
#         chiose_C = input(">>>")
#         if chiose_C == 1:
#             print("一个半小时到家，爸爸在家，拿棍等你")
#             continue
#         else:
#             print("两个小时到家，妈妈已做好了战斗准备。")
#             continue

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



#   16、制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进⾏任意现实
#       如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
name = input("input name:")
did = input("input 地点:")
aihao = input("input 爱好:")
print("敬爱可亲的{}，最喜欢在{}地⽅⼲{}".format(name,did,aihao))
#   17、等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输⼊”，并允许⽤户重新输⼊并打印。
#   敏感字符：“⼩粉嫩”、“⼤铁锤”
s = "⼩粉嫩⼤铁锤"
while True:
    i = input(">>>")
    if i in s:
        print("存在敏感字符请重新输⼊")
        continue
else:
    print("完成")

lst = ['⼩粉嫩', '⼤铁锤']
while True:
    i = input(">>>").strip()
    for n in lst:
        if n.find(i) >= 0:
            print("存在敏感字符请重新输⼊")
            break
    else:
        print("完成")


#   18、写代码，有如下列表，按照要求实现每一个功能
#       li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#       1)计算列表的长度并输出
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(len(li))
#       2)列表中追加元素"seven", 并输出添加后的列表
li.append("seven")
print(li)
#       3)请在列表的第1个位置插入元素"Tony", 并输出添加后的列表
li.insert(0, "Tony")
print(li)
#       4)请修改列表第2个位置的元素为"Kelly", 并输出修改后的列表
li[1] = "Kelly"
print(li)
#       5)请将列表l2 = [1, "a", 3, 4, "heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加
l2 = [1, "a", 3, 4, "heart"]
li = li + l2
print(li)
#       6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
#       7)请给列表添加元素"eric", 并输出添加后的列表
li.append("eric")
print(li)
#       8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
li.pop(1)
print(li)
#       9)请删除列表中的第2至4个元素，并输出删除元素后的列表
del(li[2:4])
print(li)
#       10)请将列表所有得元素反转，并输出反转后的列表
li.reverse()
print(li)
#       11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
print(li.count("alex"))

#   19、写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5, "c"]
#       li = [1, 3, 2, "a", 4, "b", 5, "c"]
#           1)通过对li列表的切片形成新的列表l1, l1 = [1, 3, 2]
l1 = li[0:3]
print(li)
#           2)通过对li列表的切片形成新的列表l2, l2 = ["a", 4, "b"]
l2 = li[3:6]
print(l2)
#           3)通过对li列表的切片形成新的列表l3, l3 = ["1,2,4,5]
l3 = li[::2]
print(l3)
#           4)通过对li列表的切片形成新的列表l4, l4 = [3, "a", "b"]
l4 = li[1:6:2]
print(l4)
#           5)通过对li列表的切片形成新的列表l5, l5 = ["c"]
l5 = li[-1]
print(l5)
#           6)通过对li列表的切片形成新的列表l6, l6 = ["b", "a", 3]
l6 = li[-3::-2]
print(l6)
#   20、写代码，有如下列表，按照要求实现每一个功能。
#       lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#           1)将列表lis中的"tt"变成大写（用两种方式）。
lis[3][2][1][0] = "TT"
print(lis)
#           2)将列表中的数字3变成字符串"100"（用两种方式）。

#           3)将列表中的字符串"1"变成数字101（用两种方式）。
#   21、请用代码实现：
#       li = ["alex", "eric", "rain"]
#       利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
li = ["alex", "eric", "rain"]
print("_".join(li))


#   22、利用for循环和range打印出下面列表的索引。
#       li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in range(len(li)):
    print(i)
#   23、利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
lst = []
for i in range(100,2):
    lst.append(i)
print(lst)
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
#   25、利用for循环和range从100~1，倒序打印。
for i in range(100, 0, -1):
    print(i)
#
#   26、利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
ls1 = list(range(100, 10, -2))
ls2 = []
for j in ls1:
    if j % 4 !=0:
        continue
    else:
        ls2.append(j)
print(ls2)


#   26、利用for循环和range，将1 - 30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成 *。
lst = list(range(1,30))
for i in lst:
    if i % 3 == 0:
        lst[lst.index(i)]="*"
print(lst)
#   27、查找列表li中的元素，移除每个元素的空格，并找出以
#       "A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中, 最后循环打印这个新列表。
#       li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
ls1 = []
for i in li:
    i = i.strip()
    print(i)
    if i.startswith('A') or i.startswith('a') and i.endswith('c'):
        ls1.append(i)
for j in ls1:
    print(j)
#   28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
#       敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
#       则将用户输入的内容中的敏感词汇替换成等长度的 *（苍老师就替换 ** *），
#       并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
pl = []
while True:
    pinglun = input(">>输入评论内容(退出q)：")
    if pinglun == 'q':
        break
    for i in range(len(li)):
        pass
    else:
        pl.append(pinglun)
        continue
print(pl)
#   29、有如下变量（tu是个元祖），请实现要求的功能
#
#       tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
#           a.讲述元祖的特性
#               元祖是只读的，不可以做增删改
#           b.请问tu变量中的第一个元素"alex"是否可被修改？
#            不可以
#           c.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
#               列表，可以被修改tu[1][2]['k2']="Seven"
#           d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
#               元祖：可以被修改tu[1][2]['k3']="Seven"
#   30、字典dic, dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
#       a.请循环输出所有的key
for i in dic:
    print(i)
#       b.请循环输出所有的value
for i in dic:
    print(dic[i])
#       c.请循环输出所有的key和value
for k,v in dic.items():
    print(k,v)
#       d.请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典'
dic['k4'] = 'v4'
print(dic)
#       e.请在修改字典中"k1"对应的值为"alex"，输出修改后的字典
dic['k1'] = 'alex'
print(dic)
#       f.请在k3对应的值中追加一个元素44，输出修改后的字典
dic['k3'].append(44)
print(dic)
#       g.请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
dic['k3'].insert(0,18)
print(dic)
# 31
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
#
#       a, 给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个元素：'量很大'。
av_catalog["欧美"]["www.youporn.com"].append('量很大')
#       b, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。
av_catalog["欧美"]["x-art.com"].pop()
#       c, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收  费,屌丝请绕过"删除。
av_catalog["欧美"]["x-art.com"].remove(("全部收  费,屌丝请绕过".replace(' ', '')))
#       d, 将此["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]列表的"verygood"全部变成大写。
av_catalog["日韩"]["tokyo-hot"][-1] = dic["日韩"]["tokyo-hot"][-1].upper()
#       e, 给'大陆'对应的字典添加一个键值对'1048': ['一天就封了']
av_catalog["大陆"]["1048"] = '一天就封了'
#       f, 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"]键值对。
av_catalog["欧美"].pop("letmedothistoyou.com")
#       g, 给此["全部免费,真好,好人一生平安", "服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
av_catalog['大陆']["1024"][0] += '可以爬下来'
#   32、有字符串
#           "k:1|k1:2|k2:3|k3:4"
#       处理成字典
#           {'k': 1, 'k1': 2....}
#
#   33、元素分类
#       有如下值li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]，将所有大于66的值保存至字典的第一个key中，
#       将小于66的值保存至第二个key的值中。
#       即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
dic = {"key": [], 'key2': []}
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
for i in li:
    if i > 66:
        dic[key2].append(i)
    else:
        dic[key1].append(i)
print(dic)
#   作业：购物车
#       1.用户先给自己的账户充钱：比如先充3000元。
#       2.页面显示序号 + 商品名称 + 商品价格，如：
#            1 电脑 1999
#            2 鼠标 10
#              …
#           n购物车结算
#       3.用户输入选择的商品序号，然后打印商品名称及商品价格, 并将此商品，添加到购物车，用户还可继续添加商品。
#       4.如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#       5.用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，
#           则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
#       6.用户输入Q或者q退出程序。
#       7.退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
