#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: school_class.py
@time: 2018/12/19 11:55
"""
"""
新式类：
    super(Student,self).__init__(self, name, age, sex)
经典类：
    SchoolMember.__init__(self, name, age, sex)
区别1：
新式类定义
class Person(object):
    super
经典类：
class Person:
    Person.__init__(self):
区别2：
    继承顺序的区别，多继承时，继承顺序的区别
    python3 无区别，python2有区别
    python3 广度查找
    Python2 先深度查找，再广度查找
    
"""


class SchoolMember(object):
    """
    学校成员基类

    """
    member = 0
    def __init__(self,name,age,sex):
        """

        :param name:姓名
        :param age: 年龄
        :param sex: 性别
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.enrool()

    def enrool(self):
        """
        注册
        :return:
        """
        print("just enroolled a new school member [%s]" %self.name)
        SchoolMember.member +=1

    def tell(self):
        print("-----info:%s------" % self.name)
        for k,v in self.__dict__.items():
            print("\t", k, v)
        print("--------end:%s------" % self.name)

    def __del__(self):
        print("开除了【%s】" % self.name)
        SchoolMember.member -= 1

class Teacher(SchoolMember):
    """
    讲师类
    """
    def __init__(self,name, age, sex, salary, course):
        """


        :param name: 姓名
        :param age: 年龄
        :param sex: 性别
        :param salary: 工资
        :param course: 课程
        """
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print("Tracher [%s] is teaching [%s]" % (self.name, self.course))

class Student(SchoolMember):
    """
    学生类
    """

    def __init__(self,name, age, sex, course, tuition):
        """

        :param name: 姓名
        :param age: 年龄
        :param sex: 性别
        :param course: 课程
        :param tuition: 学费
        """
        # 实现方法1  经典类写法
        SchoolMember.__init__(self, name, age, sex)
        # 实现方法2  新式类方法
        super(Student,self).__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print("student %s has just paied %s" % (self.name, amount))
        self.amount += amount

t1 = Teacher("Wusir", 28, "F*M", 3000, "python")
s1 = Student("Haitao", 38, "M", "pys15", 3000000)
s2 = Student("LiChuang",12,"M","pys15", 11000)
t1.tell()
s1.tell()
s2.tell()
# print(t1.__dict__)
print(SchoolMember.member)
