#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 面向对象.py
@time: 2018/12/13 14:36
"""
def person(name,age,sex,job):
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job
    }
    return data

def dog(name,dog_type):
    data = {
        'name':name,
        'type':dog_type
    }
    return data



def bark(d):
    print("dog %s: wang wang wang" %d['name'])

def walk(p):
    print("person %s is walking..." %p['name'])



d1 = dog("李峰","藏獒")  # 代表狗

p1 = person("张三", 29, "F", "运维")   # 定义一个人

p2 = person("李四", 35, "F", "Teacher")  # 定义一个人

# 调用狗的功能
bark(d1)

# 人不能调用狗的功能
bark(p2)

# 调用人的功能
walk(p1)

# 进行升级
def person(name,age,sex,job):
    def walk(p):
        print("person %s is walking..." % p['name'])
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job,
        'walk':walk
    }
    return data

def dog(name,dog_type):
    def bark(d):
        print("dog %s: wang wang wang" %d['name'])
    data = {
        'name':name,
        'type':dog_type,
        "animal_type":'dog',
        'bark':bark
    }
    return data

d1 = dog("李峰","藏獒")  # 代表狗

p1 = person("张三", 29, "F", "运维")   # 定义一个人

p2 = person("李四", 35, "F", "Teacher")  # 定义一个人

print(d1['bark'](d1))

print(p2['walk'](p2))

"""
不同的种类，有相同属性。
示例cs,警察和恐怖分子有很多相同属性，也有不同的属性，上面的方法就不好实现了，

接下来就讲到 面向对象
"""

# 1、变成范式
# 2、面向过程