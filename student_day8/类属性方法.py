#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 类属性方法.py
@time: 2018/12/24 9:52
"""


class Flight(object):
    """
    Flight status checking class
    """
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("Chenking flight %s status" % self.flight_name)
        return 1

    @property  # 属性方法不可像调用函数那样调用，属性方法就是变为 一个变量的方法，默认是只读的，不可以直接修改，如果修改使用setter属性方法
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("Flight got canceled.....")
        elif status == 1:
            print("Flight is arrived")
        elif status == 2:
            print("Flight has departured already")
        else:
            print("cannot confirm the flight status....,please check later")

    @flight_status.setter   # 修改属性值方法
    def flight_status(self, status):
        status_dic = {
            0: "canceled",
            1: "arrived",
            2: "departured"
        }
        print("\033[31;1mHas changed the flight status to \033[0m",status_dic.get(status))

    @flight_status.deleter # 删除属性方法，即删除修改后的变量
    def flight_status(self):
        print("status got removed")

    def __str__(self):
        return "<flight: %s, stauts:%s>" %(self.flight_name,self.flight_status)

    def __call__(self, *args, **kwargs):
        print("--call",args, kwargs)

    def __getitem__(self, item):
        # print("get item", item)
        return 22

    def __setitem__(self, key, value):
        print("get item key:%s, get item value:%s" % (key, value))

    def __delitem__(self, key):
        print("__delitem__",key)
if __name__ == "__main__":
    f = Flight("CA980")
    # __str__ 方法，直接返回值，不使用__str__方法，返回的是一个内存对象
    # print(f)

    # call()方法使用
    f()
    f("abc")

    # 触发__getitem__
    print("---"*30)
    print(f["age"])

    # 触发 __setitem__
    # alxe = f['name']
    f['name'] = "alex"
    print("########")
    print(f['name'])

    # 删除__delitem__
    del f["name"]

# f.flight_status
# f.flight_status = 2
# f.flight_status
# del f.flight_status    # 删除当前修改的状态，返回原来的状态
"""
f.flight_stauts = 2
del f.flight_status
此时 f.flight_stauts = 1
返回：
    Flight is arrived
    status got removed
"""
# print(f.__doc__)
# print(f.__module__)   # 当前执行的模块是自己main,当前所在模块
# print(f.__class__)    #当前执行的类是哪个

