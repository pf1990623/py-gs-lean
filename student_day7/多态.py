#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 多态.py
@time: 2018/12/19 14:38
"""
"""
python 不直接支持多态，可以间接实现
多态:
"""
class Animal:

    def __init__(self,name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subckass must umolement abstract mothod")  #主动报错

class Cat(Animal):

    def talk(self):
        return "meow"

class Dog(Animal):

    def talk(self):
        return "Woo woo"
a = Cat("xiaofeng")
b = Dog("xiaofeng")


