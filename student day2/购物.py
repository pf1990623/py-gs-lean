matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i, num in enumerate(matrix):
    print(i, num)


goods = {
    '1': {'name': '手机', 'price': 1999},
    '2': {'name': '电脑', 'price': 8000},
    '3': {'name': '背包', 'price': 200},
    '4': {'name': '鼠标', 'price': 50}
}

my = {
    'account': 0,  # 充值金额
    'shopping_cart': {},  # 已购买物品列表
    'deal_list': {}  # 成交列表
}

while True:
    money = input('请给账户充值金额(整数):').strip()
    if money.isdigit():
        my['account'] = int(money)
        break
    else:
        print('充值失败,请重新充值:')

while True:
    print('商品列表'.center(26, '*'))
    for i in goods:
        print(i, goods[i]['name'], goods[i]['price'])

    x = input('请选择商品序号 N结算退出 Q退出:')
    if x in goods:  # 在我的商品列表里面
        count = my['shopping_cart'].setdefault(x, 0)
        my['shopping_cart'][x] = count + 1  # {'商品编号': 商品数量}

    elif x.upper() == 'Q':
        break

    elif x.upper() == 'N':
        num = 0
        for i in my['shopping_cart']:
            num = num + goods[i]['price'] * my['shopping_cart'][i]  # 商品价格 * 购买的数量
        if num > my['account']:  # 金额不足
            for i in my['shopping_cart']:
                print(i, goods[i]['name'], goods[i]['price'], my['shopping_cart'][i])  # 商品名称 商品价格 商品数量
            xx = input('结算失败,请删除部分商品:')
            if xx in my['shopping_cart']:  # 删除商品
                my['shopping_cart'].pop(xx)

        else:  # 金额足够
            print('已购商品'.center(26, '*'))
            print('商品加入购物车成功')
            for i in my['shopping_cart']:
                print(goods[i]['name'], goods[i]['price'], my['shopping_cart'][i])  # 商品名称 商品价格 商品数量
            my['account'] -= num  # 扣钱
            print('本次消费金额%s, 余额%s' % (num, my['account']))
            break
    else:
        print('没有此商品,请重新输入:')