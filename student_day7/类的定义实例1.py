#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 类的定义实例1.py
@time: 2018/12/17 16:13
"""

#  定义类
class persion():
    def __init__(self,name):  # self==实例化后p,name 相当于参数名，初始化方法
        """

        如果想其他方法调用，需要在__init__（）方法中定义
         :param name:
        """
        self.NAME = name   # p.NAME=alex



    def eat(self, food):   # 类的方法
        """
        为什么写self?
            把实例本身添加进来

        :param food:
        :return:
        """
        print("%s is eating %s " % (self.NAME, food))

    def up(self):  # self = persion  # 类的方法
        print("up up  %s " % self.NAME)  # self.NAME = p.name = persion("alex")


# 实例
p = persion("alxe")  # 实例化后产生的对象叫做实例 ，类的实例化过程
#                   # p = person("alxe") = persion(p,"alex") p == self, name = alex
# 调用类的功能
p.eat("香肠")   # 调用person类的eat功能,food = 香肠，self = p
p.up()         # 调用person类的up功能

