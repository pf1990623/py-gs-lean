username = input("username:")
password = input("password:")

'''
    单条件if语句
    if 条件：
        执行。
    else：
        执行。
    注意格式！
'''

if username == "alber" and password == "abcd1234": #如果条件成立
    print("welcome to ", username)  #执行的代码
else:   #反之条件不成立
    print("wrong username or password")  #执行的代码