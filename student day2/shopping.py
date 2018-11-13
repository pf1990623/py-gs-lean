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
#
# shop_list = [['电脑', 1999], ['鼠标', 100], ['MAC', 12800], ['book', 200], ["Iphone", 12800]]
# shopping = []
# while True:
#     money = input("Money>>").strip()
#     if money.isdigit():
#         money = int(money)
#     else:
#         print("请输入人民币数字")
#         continue
#     while True:
#         for i, shop in enumerate(shop_list, 1):
#             print('\t', i, shop[0], shop[1])
#         chose = input("商品号码>:")
#         if chose != 'quit':
#             if chose.isdigit():
#                 chose = int(chose)
#                 if chose > len(shop_list):
#                     print("商品不存在")
#                     continue
#                 chose = chose - 1
#                 if money > shop_list[chose][1]:
#                     shopping.append(shop_list[chose])
#                     money -= shop_list[chose][1]
#                     print("Remaining money: %s" % money)
#                 else:
#                     print("can not afford")
#         elif chose == 'n':
#             money -= shop_list[chose][1]
#             for j in shopping:
#                 print(j[0], j[1])
#             print("剩余金额：%s" % money)
#         elif chose == 'q':
#             exit()

shop_list = [['电脑', 1999], ['鼠标', 100], ['MAC', 12800], ['book', 200], ["Iphone", 12800]]
shopping = []
while True:
    tmp = 0
    tmp1 = 0
    money = input("Money>>").strip()
    if money.isdigit():
        money = int(money)
    else:
        print("请输入人民币数字")
        continue
    while True:
        for i, shop in enumerate(shop_list, 1):
            print('\t', i, shop[0], shop[1])
        chose = input("商品号码>:")
        if chose.isdigit():
            chose = int(chose)
            if chose > len(shop_list):
                print("商品不存在")
                continue
            chose = chose - 1
            shopping.append(shop_list[chose])
            tmp += shop_list[chose][1]
            print(tmp)
        elif chose == 'n':
            tmp1 = money - tmp
            if tmp1 > 0:
                for j in shopping:
                    print(j[0], j[1])
                print("剩余金额：%s" % money)
                exit()
            elif tmp1 <= 0:
                print(money)
                money = input("充值Money>>").strip()
                if money.isdigit():
                    money = int(money)
                    print(money)
                    money = money + tmp1
                    print(money)
                    if money > 0:
                        for j in shopping:
                            print(j[0], j[1])
                        print(money)
                        print("剩余金额：%s" % money)
                        exit()
        elif chose == 'q':
            exit()
