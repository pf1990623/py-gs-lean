#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: models.py
@time: 2018/12/20 14:16
"""
import time
import pickle
import os
from conf import settings
from src import identifier


class BaseModel:
    def save(self):
        file_path = os.path.join(self.db_path,str(self.nid))
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_all_obj_list(cls):
        ret = []
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path, filename)
            obj = pickle.load(open(file_path, 'rb'))
            ret.append(obj)
        return ret
# a1=Admin(xiao,123)
# a1.db_path
# a1,save()
# a2 a3 a4
# ret=Admin.get_all_obj_list()  --->[a1_obj,a2_obj,a3_obj

class Admin(BaseModel):

    db_path = settings.ADMIN_DB_DIR

    def __init__(self, username, password):
        self.nid = identifier.AdminNid()
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login():
        try:
            name = input("请输入用户名：").strip()
            pas = input("请输入密码：").strip()
            for obj in Admin.get_all_obj_list():
                status = True
                error = ''
                data = '\033[45;1m登录成功\033[0m'
                break
            else:
                raise Exception('\033[43;1用户名会密码错误\033[0m' %name)
        except Exception as e:
            status = False
            error = str(e)
            data = ''
        return {'status':status,'error':error,'data':data}


class School(BaseModel):

    db_path = settings.SCHOOL_DB_DIR

    def __init__(self,name, addr):
        """
        :param name: 学校名字
        :param addr: 学校地址
        """
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.__income = 0

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    """
    s1 = School("老男孩“，“北京”）
    c1 = Course("python,11000,4,s1.nid)
    c1.school_nid_get


    """
    db_path = settings.TEACHER_DB_DIR

    def __init__(self,name, level):
        """

        :param name: 老师名字
        :param level: 老师级别
        """
        self.nid = identifier.TeacherNid(self.db_path)
        self.name = name
        self.level = level
        self.__account = 0  # 老师的账户
        self.create_time = time.strftime('%Y-%m-%d %X')

class Course(BaseModel):

    db_path = settings.COURSE_DB_DIR

    def __init__(self, name, price, period, school_nid):
        """
        :param name: 课程名字
        :param price: 课程价格
        :param period: 课程周期
        :param school_nid: 学校ID
        """
        self.nid = identifier.CourseNid(self.db_path)
        self.name = name
        self.price = price
        self.period = period
        self.school_nid = school_nid


class Course_to_teacher(BaseModel):

    db_path = settings.COURSE_TO_TEACHER_DB_DIR

    def __init__(self, course_nid, school_nid):
        self.nid = identifier.Course_to_teacherNid(self.db_path)
        self.course_nid = course_nid
        self.school.nid = school_nid

    def get_course_to_teacher_list(self):
        ret = self.get_all_obj_list()
        if ret:
            return [ret.course_nid.get_obj_by_uuid(), ret.classes_nid.get_obj_by_uuid()]
        return [None,None]

class Classes(BaseModel):

    db_path = settings.CLASSES_DB_DIR

    def __init__(self, name,tuition,school_nid,course_to_teacher_list):
        """
        :param name: 班级名字
        :param tuition:  学费
        :param school_nid:  学校 ID
        :param course_to_teacher_list:
        """
        self.nid = identifier.ClassesNid(self.db_path)
        self.name = name
        self.tuition = tuition
        self.school_nid = school_nid
        self.course_to_teacher_list = course_to_teacher_list


class Score:

    def __init__(self, nid):
        """
        :param nid: 成绩nid号
        """
        self.nid = nid
        self.score_dict = {}

    def set(self, course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self, course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)



class Student(BaseModel):

    db_path = settings.STUDENT_DB_DIR

    def __init__(self, name, age, qq, classes_nid):
        """
        :param name: 学生姓名
        :param age: 学生年龄
        :param qq: 学生qq号
        :param classes_nid:  班级id
        """
        self.nid = identifier.StudentNid(self.db_path)  # identifier模块下的StudentNid对象中的db_path = 学生的目录信息
                                                        # self 实例化后的学生对象
        self.name = name
        self.age = age
        self.qq = qq
        self.classes_nid = classes_nid
        self.score = Score(self.nid)  # 成绩










