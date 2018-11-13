
# login_status = False
#
# def auth():
#     # get data from db
#     _username = "xiaofeng"
#     _password = '123456'
#     username = input("username:").strip()
#     password = input("password:").strip()
#     if username == _username and password == _password:
#         print("password authentication")
#         # global login_status
#         # login_status = True   # 官方成为局部变量，只在当前函数生效
#         return True    # 如果不指定返回值，函数会自动添加一个返回值为none
#     else:
#         return False
# login_status = auth()
# def home():
#     if login_status == True:
#         print("welcome to page")
#     else:
#         auth()
#
#
# def pay():
#     if login_status == True:
#         print("welcome to page")
#     else:
#         auth()
#
# home()
# pay()

# 返回值的作用:
#       1、一旦你的函数经过调用，并开始执行,那你的函数的外部的程序就没有办法再控制函数的执行过程
#            此时外部程序只能安静的等待函数的执行结果,为啥要等待函数结果，因为外部程序要根据函数的执行结果来决定下一步怎样走
#           这个结果就是以return的形式返回给外部程序
#       2、return代表一个函数的结束，
#       3、return 可以返回任意数据类型
#       4、对于用户角度，函数可以返回任意数量的值，但对于py本身来讲，函数只能返回一个值

# 局部变量

# 嵌套函数, 函数递归
def changeName():
    name = "xiaofeng"
    print(name)

    def changeName2():
        name = "panfeng"
        print(name)
    changeName2()

changeName()

# 递归函数
# 如果函数在内部调用自身，这个函数就是递归函数
# 递归最大范围999层
# def func(n):
#     print("----",n+1)
#     func(n+1)
#
# func(0)

def calc(n):
    print(n)
    if n // 2 > 0:
        calc(n//2)
calc(10)


def calc(n):

    if n // 2 > 0:
        calc(n//2)
    print(n)

calc(10)

# 必须有一个明确的条件
# 每进入更深一层递归是，为题的规模相比上次递归都应有所减少
# 递归的效率不高，递归层次过多，会导致栈溢出

data = [3, 5, 10, 12, 14, 17, 11, 19, 20, 19]
# 判断一个数是否在列表，排除内置方法
# 1、排序
data.sort()

def binary_search(datasets, find_num):
    if len(datasets) > 0:
        middle_pos = int(len(datasets) / 2)
        print(middle_pos)
        if datasets[middle_pos] == find_num:
            # find it
            print("Find Number", datasets[middle_pos])
        elif datasets[middle_pos] > find_num:
            # data in left side
            print("\033[31;1m going left side\033[0m", datasets[0:middle_pos], datasets[middle_pos])
            binary_search(datasets[0:middle_pos], find_num)
        else:
            print("\033[32;1m going right side\033[0m", datasets[middle_pos+1:], datasets[middle_pos])
            binary_search(datasets[middle_pos+1:], find_num)
    else:
        print("not find the num", find_num)
binary_search(data, 15)