# 购物车
product = [
    ['Iphone',5800],
    ['Mac',12800],
    ['book',300],
    ['Watch',2000],
    ['coffer',30]
]
shopping_list = []
while True:
    gongzi = input("工资(元)：")
    if gongzi.isdigit():
        gongzi = int(gongzi)
        break
while True:
    for i,j in enumerate(product):
        print(i,j[0],j[1])
    chiose = input("输入商品编号(退出quit):")
    if chiose.isdigit():
        chiose = int(chiose)
        if 0 <= chiose < len(product):
            product_list = product[chiose]
            print(product_list)
            if product_list[1] <= gongzi:
                gongzi -= product_list[1]
                shopping_list.append(product_list)
                print("买的起",gongzi)
            else:
                print("买不起")
        else:
            print("商品编号不存在")
    elif chiose == 'quit':
        for key in shopping_list:
            print(key)
        print(gongzi)
        exit()
    else:
        print("请输入正确的商品编号")
    # break
