import auth
"""
此方法调用，需要写模块名+函数名
例如 auth模块的login方法，就要使用下面的方法：
    auth.login
另外一种方法from 导入模块
from 模块名 import 函数名
"""
def home():
    print("--------首页--------")

def America():
    print("------美国专区------")
@auth.login
def henan():
    print("------河南专区------")
@auth.login
def Japan():
    print("------日韩专区------")

# home()
# America()  # inner加上括号执行inner函数
# Japan()
# henan()

"""
如下是from导入方法示例,此种方法不需要使用模块名+函数名，可以直接调用函数名

"""

from auth import login

def America():
    print("------美国专区------")
@login
def henan():
    print("------河南专区------")
@login
def Japan():
    print("------日韩专区------")

home()
America()  # inner加上括号执行inner函数
Japan()
henan()