#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 反射.py
@time: 2018/12/25 10:39
"""
"""
# 反射

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
# hasattr(容器,'名称')    # 以字符串形式，判断某个"对象"中是否含有指定的元素
# getattr(容器,'名称' )   # 义字符串形式去某个"对象"中获取指定的属性
# setattr(容器,'名称',值) # 以字符串的形式，去某个"对象"中设置指定属性
# delattr(容器,'名称')    #  以字符串形式去删除某个"对象"中的指定属性
# 义字符串的形式导入模块
import  time
# v = __import__("time")
while True:
    try:
        inp = input("输入url:").strip()
        m, n = inp.split('/')
        module = __import__('controller.%s' %m, fromlist=True)
        if hasattr(module,n):
            func = getattr(module,n)
            result = func()
        else:
            result = 404
    except Exception as e:
        result = 500
    print(result)

