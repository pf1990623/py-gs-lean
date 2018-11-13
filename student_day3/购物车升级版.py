def my_register(user, passwd):  # 注册函数
    with open('user_pass', encoding='utf-8') as f1:  # 只读方式打开文件对比当前用户
        file = f1.readlines()
        for i in file:
            i = i.strip().split(':')
            if user in i[1]:  # 判断用户是否存在
                return ('用户%s已存在,请登录.' % user)
        else:
            with open('user_pass', encoding='utf-8', mode='a') as f2:
                f2.write('帐号:{}  密码:{}\n'.format(user, passwd))
                print('用户%s注册成功.' % user)


def my_login(user, passwd):  # 登录函数
    with open('user_pass', encoding='utf-8') as f1:  # 只读方式打开文件对比当前用户
        file = f1.readlines()
        for i in file:
            i = i.strip().split(':')
            if user in i[1] and passwd == i[3]:  # 对比user_pass文件
                print('用户%s请登录成功.' % user)
                my_shop()
        else:
            print('用户%s登录失败,请重试.' % user)


def my_shop():  # 购物车函数
    product = {'1': {'name': '电脑', 'price': 200},
               '2': {'name': '手机', 'price': 300},
               '3': {'name': '楼房', 'price': 400}}
    my = {'balance': 0, 'shop_list': {}}

    while 1:  # 充值金额
        money = input('请充值金额(整数):')
        if money.isdigit():
            my['balance'] = int(money)
            break
        else:
            print('充值失败,请重试.')

    while 1:
        print('商品列表'.center(26, '*'))
        for i in product: print(i, product[i]['name'], product[i]['price'])

        inp = input('请输入购买的商品编号, N结算并退出购买, Q退出:').strip()
        if inp in product:  # 计算我买的商品数量
            count = my['shop_list'].setdefault(inp, 0)
            my['shop_list'][inp] = count + 1  # {'商品编号': 商品数量}
            print('已选择1件 %s 商品' % product[inp]['name'])
        elif inp.upper() == 'Q':
            quit()
        elif inp.upper() == 'N':  # 结算并退出购买
            num = 0
            for i2 in my['shop_list']: num += product[i2]['price'] * my['shop_list'][i2]
            if num > my['balance']:  # 余额不够
                for i3 in my['shop_list']:
                    print(i3, product[i3]['name'], product[i3]['price'], my['shop_list'][i]

