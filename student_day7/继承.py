#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 继承.py
@time: 2018/12/18 15:13
"""

"""
当同一个类的对象有共同属性和不通属性
    一个父类，连个子类
    通过继承创建的新类黑称为子类或派生类
    被继承的类被称为基类、父类或超类
    继承的过程就是从一般到特殊的过程
    要实现继承，可以通过继承和组合来实行
    一个子类可以继承多个基类，一般情况下，一个子类只能有一个基类，要实现多重继承，可以通过多级继承来实现
    
    继承实现方式主要有两类：
        1、实现继承：
            实现继承是指使用基类的属性和方法而无需额外编码的能力
        2、接口继承:
            接口继承是指仅使用属性和方法的名称，但是子类必须提供实现的能力（子类重构父类的方法）
        在考虑继承时，有一点需要注意：那就是两个类之间应该是“属于”的关系，例如 A是一个人，B也是一个人，因此这两个类
    偶可以继承person类，但是leg类却不能继承person类，因为腿不是一个人
    抽象类仅定义将子类创建的一般属性和方法
        OO开发范式大致为：划分对象--》抽象类--->将类组织成层次化结构（继承和组合）--》用类与实例进行设计和实现的几个阶段

"""
# 简答示例
class Person(object):
    """
    定义一个父类
    b = BlackPerson("wei er smith", "22",)
    子类BlackPerson实例化后，父类的slef代表的是实例对象b
    """
    def __init__(self, name, age):   # 此处的self 代表的是子类实例化后的实力名b
        self.name = name  # self = b,self.name = b.name
        self.age = age
        self.xx = "Normal"
        print("Person")
        print(self.name,self.age)
    def talk(self):
        print("person is talking.....")

class BlackPerson(Person):    # 子类继承父类Person
    """
    子类：
        实例化：
            b = BlackPerson("wei er smith", "22","strong")  实例化之后
    """

    def __init__(self, name, age):  # 先继承，再重构 self = BlackPersion
        Person.__init__(self, name, age)    # self 代表 b
        # self.strength = strength
        print(self.name, self.age)
        print(self.strength)

    def talk(self):          # 重构父类的方法，及接口继承类型
        print("black person is blaba")

    def walk(self):
        print("is walking")


class WhitePerson(Person):
    pass


b = BlackPerson("wei er smith", "22",)

