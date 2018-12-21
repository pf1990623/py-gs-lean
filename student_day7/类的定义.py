#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 类的定义.py
@time: 2018/12/17 15:41
"""

# 最基本类的定义
class Dog(object):

    def __init__(self, name):  # 构造函数，或者构造方法，===>初始化方法
        self.NAME = name    # self代表实例本身
        # d.NAME = name

    def sayhi(self):  # self代表实例本身，类的方法
        print("hello I am a dog my name is", self.NAME)   # self.NAME = d.self

    def eat(self, food):
        print("%s is eating %s" %(self.NAME, food))

"""
 未被调用的类，在内存中是存在的

"""

#  类实例化 过程
d = Dog("alex")   # 实例化name,参数值是alex, Dog(d,"alxe")，#实例化后产生的对象 叫 实例，当前类的实例
d2 = Dog("alex2")
# 调用对象功能
d.sayhi()  # d.sayhi(d)
d2.sayhi()
d.eat("香肠")
