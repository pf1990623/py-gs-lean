#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 静态方法.py
@time: 2018/12/21 17:40
"""

class Person(object):

    def __init__(self, name):
        self.name  = name

    def eat(self):
        print("xxxx----eat---%s" % self.name)

# p = Person("Jack")
# p.eat()


# 静态方法
class Person1(object):
    name = "xxxx"
    def __init__(self, name):
        self.name = name

    @staticmethod        # 静态方法 既不能访问公有属性，也不能访问实例
    def eat(name):
        print("xxxx----eat---%s" % name)

    @classmethod            # 类方法
    def walk(self):   # 类方法 只能访问类的公有属性，不能访问实例属性
        print("%s is walking" % self.name)




    @property  # 把一个方法变为一个静态属性,且是只读的，不能更改
    def talk(self):
        print("%s say..." % self.name)

    @talk.setter  # 更改静态属性方法
    def talk(self,msg):
        print("%s say..." % msg)

    @talk.deleter        # 删除属性方法
    def talk(self):
        print("delete talk....")

# Person1.eat("jack1")
#
# Person1.walk()
p1 = Person1("xxxx")
p1.talk
p1.talk = "hello"
