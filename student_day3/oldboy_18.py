# 18、 有如下函数:
#   def wrapper():
#       def inner():
#           print(666)
#   wrapper()
#   你可以任意添加代码,用两种或以上的方法,执行inner函数.

def wrapper():
    print(5555)

    def inner():
        print(666)

    inner()

wrapper()


def wrapper():
    print("555")

    inner()

def inner():
    print(666)

wrapper()


def wrapper():
    print("555")
    return inner()

def inner():
    print(666)


wrapper()
print("程序结束")