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