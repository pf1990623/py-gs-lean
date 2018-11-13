# names = ['zhangsan', 'lisi', 'wangwu']
# print(names[0])
# print(names[1])
# print(names[0:3])
#
# # 列表的其他方法
# # 列表的增
# names.append('aaa')
# print(names)
#
# #列表的插入
# names.insert(1, 'bbb')
# print(names)
# # 列表的删
# # 默认删除最后一个
# names.pop()
# print(names)
#
# #remove("指定要删除的字符")
# names.remove('bbb')
# print(names)
#
# # 根据索引删除
# del names[2]
# print(names)
#
# #列表的改
# names[1] = "wangxu"
# print(names)
#
# #列表的查
# names = ['a','b','c','d']
# print(names[0::2]) #隔两个取
# print(names[-3:])  #获取后三个
# print(names[:3])   #获取前三个
# print("------------------------")
# print(names.index("a"))
#
# #列表清空
# # names.clear()
# names.count('a')
#
# #names.extend("2wsx")  #列表的扩展，又成合并
# names.extend("2wsx")
# print(names)
# names.reverse()  #反向排序
# print(names)
# names.sort()     #排序方式是根据asicc码表进行排序
# print(names)
#
# #python3中的数字和字符串是不能排序的，而python2可以，
#
# n3 = names.copy()
# print(n3,id(names),id(n3))
# n4 = names
# print(n4,id(names),id(n4))

# 练习题：购物车程序
# 》》你的工资
#----------shop list---------
#1 iphone  5800
#2 macbook 12800
#3 coffee  30
#4 bike    2000
#>>:1
#钱不够
#>>:3
#加入购物车，扣钱
# added[coffee] into your shopping list,your current blance is 4970
# >>:quit
# >>
# you lalance is 4000
# 已购买商品，打印列表
#列表的循环
# for i in names:
#     print(i)
#
# products = {
#     "Iphone":5800,
#     "Mac":12800,
#     "coffer":30,
#     "book":200
# }
#  列表案例
#  列表购物车案例
product = [
    ["Iphone",5800],
    ["Mac",12800],
    ["coffer",30],
    ["book",200]
]

product_list = []
balance = input("输入你的工资：")
if balance.isdigit():
    balance = int(balance)
    print(balance)
while True:
    for i,j in enumerate(product):
        print(i,j[0],j[1])
    product_list_id = input("输入商品编号:")
    if product_list_id.isdigit():
        product_list_id=int(product_list_id)
        if 0 <= product_list_id < len(product):
            p_item = product[product_list_id]
            if p_item[1] <= balance:
                balance -= p_item[1]
                product_list.append(p_item[0])
            else:
                print("您够买不起，您的余额: %s" %balance)
        else:
            print("您输入的商品编码不存在")
    elif product_list_id == 'q':
        for key in product_list:
            print("您购买的商品:%s" %key)
        print("您的余额：%s" %balance)
        exit()


# for k in product_list:
#     print("您购买的商品product_list")
#     print("您的余额："balance)

