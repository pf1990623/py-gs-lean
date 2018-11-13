#作业1：博客
#作业2：编写登录几口
'''
    1、输入用户名密码
    2、认证成功后，显示欢迎信息
    3、输入三次后锁定
'''
#作业3：多级菜单
#要求：
'''
    1、三级菜单
    2、可依次进入各个子菜单
    3、所需知识点：列表、字典
'''
#

# user = "alber"
# passwd = "1234"

username = open('black','r',encoding='utf-8')
a=username.readlines()

for i in range(1,4):
    username = input("username:")

    if username in a:
        print("帐号",username,"已经锁定")
        break
    elif username == user:
        for j in range(1, 4):
            password = input("password:")
            if password == passwd:
                print("welcome to ",username)
                break
            if j == 3:
                print("帐号",username,"被锁定")
                break
        else:
            print("username or password wrong")
        if i == 3:
            print("帐号",username,"被锁定")


