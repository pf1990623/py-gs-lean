#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 总结.py
@time: 2018/12/19 14:56
"""
"""
1、什么是面向对象编程？
    以前使用函数
    类 + 对象
2、什么是类，什么是对象，又有什么关系
    class 类
        def 函数1():
            pass
        def 函数2():
            pass
    # obj是对象，实例化的过程
    obj = 类（）
    obj.函数1()

3、什么时候适合用面向对象
    1、根据一个模版来创建某些东西，例如批量生成人
    2、根据公共场景提取公共功能   
    3、当很多个函数用很多公共参数时，就可以使用面向对象

4、self就是调用当前方法的对象

5、封装
    类中封装和字段和方法
    对象中封装了：普通字段的的值
    
6、
7、  字段：
        普通字段--保存在对象中
        静态字段---保存在类中
    方法：
        普通方法---保存在类中，调用者对象,至少有一个self参数
        class F1:
            def __init__(self,name)
                self.name = name
            def a1(self):
                print(self.name)
        
        静态方法： 保存在类中，调用者类（无需创建对象，）可以有任意个参数
            class F1:
                @staticmethod
                def a1():
                    print("alex")
            F1.a1()


"""
class F1:
    def __init__(self, n):
        self.N = n  # alex
        print("F1")

class F2:
    def __init__(self, arg1):
        self.a = arg1  # arg1  o2.a = o1
        print("F2")

class F3:
    def __init__(self, arg2):
        self.b = arg2  # arg2=o2  o3.b == o2
        print("F3")

o1 = F1('alex')
o2 = F2(o1)
o3 = F3(o2)

# 输出ALex
print(o3.b.a.N)