"""
网站想收费，必须先认证，认证成功后，然后进行判定


"""
'''

user_status = False
def login(func):
    __username = "xiaofeng"
    __password = "xiaofeng"
    global user_status
    if user_status == False:
        username = input("user:")
        password = input("password")
        if username == __username and password == __password:
            print("welcome to login")
            user_status = True
        else:
            print("wrong username or password")
    if user_status == True:
        func()     # 只要通过验证，就执行想用的函数


def home():
    print("--------首页--------")

def America():
    print("------美国专区------")

def henan():
    print("------河南专区------")

def Japan():
    print("------日韩专区------")

home()
America()
henan()
Japan()
'''

"""
需求：因用户访问量大，增加了网络带宽，需要对河南和美国视频模块进行收费
考虑到 之前该接口已经被其他的用户调用，
开发的开放封闭原则：
    对源代码进行封闭
    对扩展进行开放
进行如下修改
"""
user_status = False
def login(func):
    def inner():
        __username = "xiaofeng"
        __password = "xiaofeng"
        global user_status
        if user_status == False:
            username = input("user:")
            password = input("password:")
            if username == __username and password == __password:
                print("welcome to login")
                user_status = True
            else:
                print("wrong username or password")
        if user_status == True:
            func()     # 只要通过验证，就执行想用的函数
    return inner

def home():
    print("--------首页--------")

def America():
    print("------美国专区------")
@login
def henan():
    print("------河南专区------")
@login
def Japan():
    print("------日韩专区------")


# America = login(America())  # America是inner函数，但是没有执行、
# henan = login(henan())
# print(America)
home()
America()  # inner加上括号执行inner函数
Japan()
henan()





"""
    开放封闭原则：
        封闭：已实现的功能代码块
        开放：对扩展开发
        
    高阶函数：
        把一个函数当作一个参数，传递给另一个函数
        
    嵌套函数：
        
不改变原有代码，不改变原有调用方式下，添加了功能

语法糖：官方名称装饰器
装饰器的调用方法@开通，需要哪个函数调用，就需要在该函数的上方写@函数名
作用：
    万全符合开发规则，开放--封闭原则：
        1、不改变原有功能代码，不改变原有调用方式，实现扩展新的功能
"""



# def plus(n):
#     return n+1
#
# plus2 = lambda x:x+1
#
# print(plus(2))
# print(plus2(2))