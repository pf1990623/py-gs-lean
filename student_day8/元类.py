#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 元类.py
@time: 2018/12/24 11:26
"""

"""

类是由type产生的
"""
# 特殊方法，动态创建类


def talk(self,msg):
    print("%s istalking :%s" %(self.name, msg))


def __init__(self,name):
    self.name = name


Dog = type("Dog",(object,),{"talk":talk,"__init__":__init__})

print(type(Dog))

"""
type第一个参数：类名
type第二个参数：当前类的基类
type第三个参数：类的成员

"""
# 特殊方法，动态创建类


def func(self):
    print("hello %s"%self.name)


def __init__(self,name,age):
    self.name = name
    self.age = age


Foo = type('Foo', (object,), {'func':func,'__init__': __init__})

f = Foo("jack",22)
f.func()
"""
类默认是由type类实例化产生，type类中如何实现创建类，类又如何创建对象
答：
    类中有一个属性

"""