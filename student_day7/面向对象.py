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

"""
面向对象简称：oop：object oriented programing  面向对象变成
    OOP编程是用“类”和“对象”来创建各种模型来实现对真实世界的描述，使用面向对象变成的原因：
        一方面： 是因为它可以使程序的维护和扩展变的简单，并且可以大大提高程序的开发效率
        另一方面：基于面向对象的程序可以使它人更加容易的理解你的代码逻辑，从而使团队开发变的更从容。
class 类，模版
    一个类即一类拥有相同属性的对象的抽象，蓝图、原型、 在类中定义了这些对象的都具有属性、共同的方法

object 对象:
    通过造人模版，造成的人，人即是对象， 中间的过程叫做“实例化”
    一个对象即是一个类的实例化后的实例，一个类必须经过实例化后方可在程序中调用，一个类可以实例化多个对象，每个对象亦可以用不通
    的属性，就像人类所有的人，每个人是指具体的西乡，人与人之前的共性，亦有不同。
    
Encapsublation 封装
    在类中对数据的赋值，内部调用对外部用户是透明的，这使类变成了一个胶囊或容器，里面包含着类的数据和方法
    特性：
        1、防止数据被随意修改
        2、使外部程序不需要关注对象内部的构造，或内部逻辑结构，只需要通过此对象对外提供的接口，进行直接访问即可。

Inheritance 继承
    一个类可以派生出子类，在这个父类定义的属性、方法自动被子类继承。
    通过父类，子类的方式以最小代码量的方式实现不同角色的共同点和不同点
    实例：  cs, 都有人的属性，生命值，  在定义一个警察的类，一个匪徒的类，同时继承父亲类的属性
    
Polymorphism 多态
        多态是面向对象的重要特性，简单点说：“一个借口，多种实现”，指一个基类中派生了不同的子类，且每个子类在继承了同样的方法名的同时
    又对父类的方法做了不通的实现，这就是同一种事物表现的多种形态。
        示例：
            人类功能：  语言
                子类：黑人：语言
                子类：白人：语言
                子类：黄种人：语言
            黑人和白人继承了父类的语言功能，但同时 又对语言这个功能进行了不同的实现，及黑人将黑人语言，白人讲英语
                
                
        编程其实就是一个将具体世界进行抽象化的过程，多态就是抽象化的一种体现，把一系列具体事物的共同点抽象出来，再通过这个抽象的事物，
    与不同的具体事物进行对话。
    
        对不同类的对象发出相同的小徐将会有不同的行为，比如，你的老板让所有的员工在9点钟开始工作，他只要在9点的时候说，开始工作即可。
    而不需要对销售人员说：开始销售工作，对技术人员说：开始技术工作，运维员工是一个抽象的事物，只要是员工就可以开始工作，这一点就行。至于
    每个员工，当然会各司其职，做各自的工作。
    
        多态允许将子类的对象当作父类的抽象对象使用，某父类型的引用指向其子类型对象，调用的方法是该子类的方法。这里引用和调用方法的代码前
    就已经决定了，而引用所指向的对象可以在运行期间动态绑定

面向对象编程（object oriented programming） 介绍
    对于变成语言的初学者来讲，OOP不是一个容易理解的变成方式，大家虽然按照老师讲的都知道OOP的三个特性是：封装、继承、多态，并且大家已经
知道如何定义类、方法等面向对象的常用语法，但是一到真正写程序的时候，还是很多人喜欢用函数式编程来写代码，特别是初学者，很容易陷入窘境，我
知道面向对象，我也会写类，但我依然没发现在使用面向对象后，对我们的程序开发效率或其他方面带来好处，因为我使用的函数编程就可以减少重复代码
做到程序扩展，为啥子还用到面向对象，

无论以什么样的形式来编程，我们都要明确记住以下原则：
    1、写重复代码是非常比好的低级行为
    2、写的代码需要经常变更

开发正规的程序跟那种写个运行 一次就扔了的小脚本一个很大的而不同就是，你的代码总需要不断的修改，不是修改bug就是添加功能等，所以为了
日后方便程序的修改及扩展，你写的代码一定要遵循易读、易改的原则（专业术语，就做可读性好，易扩展）


"""

# 非oop是实现方法
# oop实现方法

