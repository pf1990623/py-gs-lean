product = [
    ['iphonex',9800],
    ['iphone6s',3500],
    ['Mac','12800'],
    ['coffer',30],
    ['Book',200],
    ['xiaoqiang',5888]

shopping_list = []
gongzi = input("输入工资：")
if gongzi.isdigit():
    gongzi = int(gongzi)
while True:
    for i,j in enumerate(product):
        print(i,j[0],j[1])
    choose = input("输入商品编号(quit退出)：")
    if choose.isdigit():
        choose = int(choose)
        if 0 <= choose < len(product):
            p = product[choose]
            if p[1] <= gongzi:
                gongzi -= p[1]
                shopping_list.append(p)
                print("工资剩余%s,购买的商品%s" %(gongzi,p))
            else:
                print("买不起")
        else:
            print("商品编号不存在")
    elif choose == 'quit':
        for i in shopping_list:
            print(i)
        print(gongzi)
        exit()


