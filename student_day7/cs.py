#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: cs.py
@time: 2018/12/17 16:29
"""
class Role(object):
    """
    人员信息定义

    """
    nationatily = "JP"   # 共有属性

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__herat = "Normal"  # 私有属性

    def shot(self):
        """
        射击

        :return:
        """
        print("%s shooting" % self.name)

    def got_shot(self):
        """
        中枪减血
        :return:
        """
        print("%s ah...,I got shot ..." % self.name)

    def bug_gun(self,gun_name):   # def 定义的函数本身就是共有方法
        """
        买枪

        :param gun_name:
        :return:
        """
        print("%s just bought %s " % (self.name, gun_name))
        self.weapon = gun_name    # 修改对象的属性

    def __del__(self):  # 析构方法
        """
        析构函数：程序的首尾工作，例如服务端停止，有客户端还在链接，这时候就会用到析构函数

        :return:
        """
        print("del ..... run ... ")

# 实例化
r1 = Role("student", "static", "AK47")  # 生成了一个角色

r2 = Role("Jack", "匪徒", "B22")

# 调用功能
# r1.shot()
#
# r2.bug_gun("AK47")

# Role.nationatily = "US"   # 修改所有的公用属性
# r1.nationatily = "CN"   # 通过对象更改，修改的是单个属性的公用属性


# 封装
"""
类》》》实例化》》》》实力对象

__init__构造函数
self.name = name # 属性，成员变量，字段

def sayhi()  # 方法，动态属性

公有属性和私有属性
    私有属性：不想被别人访问
        self.__heart = "Normal"
        __private_attr_name = value
        # 可以看到私有属性，但是不能更改
        def get_herat(self):
            return self.__heart
        # 私有属性，强制访问
           r1._Role__heart   # 对象名+类名+私有属性
    公有属性：
        所有属于此类的都可以访问的属性。
        在类中直接定义的数据叫公有属性
        1、共有属性修改为私有属性
        
"""

# 共有方法改私有方法
# def shot2(self):
#     print("wo lai sh ni l")
#
# r1.shot = shot2  #
# r1.shot(r1)  # 不在类中定义的self,默认是不存在的，需要单独指定
# r2.shot()
