#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence
@file: 异常处理.py
@time: 2018/12/24 14:12
"""
# 异常处理
# while True:
#     try:
#         a1 = input(">>>>")
#         a2 = input(">>>>")
#         a1 = input(a1)
#         a2 = input(a2)
#         a3 = a1 + a2
#         print(a3)
#     except Exception as e:
#         print(e)


"""
1、基本异常处理结构
    try:
        代码块
    expect Execption as e:
        代码块


2、复杂结构
    try:
        ....
    expect:
        ....
    esle:
        ....
    finally:
        ....
3、异常对象
4、异常种类
    Execption: 所有的异常都捕获
    其他:   只能处理某一种情况
5、主动触发异常
    程序分层
     raise Execption("日志内容自己定义")
6、断言
    assert 条件 ，如果条件为True,则执行下面语句，如果条件不成立，则断开
    断言日志不用去捕捉
    
7、自定义异常
    用的情况不多

重点：
    1、2、3、4、5

"""

print(1)
assert 1 == 2   # 相当于三元预算
print(2)



try:
    int("ssss")
    li = [11,22]
    li[1000]
except ValueError as e:        # 针对某一类具体信息
    print(e)  # 1.log
except IndexError as e:
    print(e)  # 2.log
except Exception as e:
    print(e)
else:
    print("正确")
finally:
    print("finnlly")


# 反射
"""
1、允许用户输入 account/login
              account/logout
              /home/index
              /home/order
2、看到不同的结果
3、404
    # web框架，路由系统
    li = {'account/login':f1,'account/logout','/home/index','/home/order'｝
    
    inp = input(">>>")
    if inp in li:
        li[inp]()
    
    # 反射
        inp = input(">>>")
    if inp in li:
        li[inp]()
        
        
"""
# 在某一个模块中找函数
# getattr() 专门去某个地府获取他内部的东西，获取的内容可以是字符串形式
# hasattr() 专门去某个地方获取内部的东西，判断东西是否存在
# hasattr(容器,'名称')   # 以字符串形式，判断某个对象中是否含有指定的元素
# getattr(容器,'名称' )  # 以去某个对象中获取指定的属性
# setattr(容器,'名称')
# delattr(容器,'名称')