#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 作业.py
@time: 2018/12/20 9:30
"""

"""
选课系统：
角色： 学校、学员、课程、老师

学校名唯一性
教师名唯一性



"""
import pickle,uuid

class BaseModel:

    def save(self):
        pickle.dump(self,open("xxx",'wb'))

    @classmethod
    def git_all_obj_list(cls):
        ret = []
        for file_name in "循环/home/db/文件名":
            obj = pickle.load(open("home/db/file_name,'rb"))
            ret.append(obj)
        return ret


class School(BaseModel):

    def __init__(self, name, addr):
        # self.身份证 = 身份证
        self.name = name
        self.name = addr

    def __str__(self):
        return self.name

    @classmethod
    def git_all_obj_list(cls):
        ret = []
        for file_name in "循环/home/db/文件名":
            obj = pickle.load(open("home/db/file_name,'rb"))
            ret.append(obj)
        return ret



s1 = School("老男孩", "北京")
s1.save()  # pickle.dump(s1,open("/home/db/老男孩,"wb")
# /home/db/s1_file
s2 = School("北大青鸟", "北京")
s2.save()  # pickle.dump(s1,open("/home/db/北大青鸟,"wb")
# /home/db/s2_file

s3 = School("老男孩", "上海")
s3.save()  # pickle.dump(s3,open("/home/db/老男孩,"wb")


# 打印所有的学校信息
for school_obj in School.get_all_obj_list():
    print('学校名字：%s' % school_obj)




class Teacher(BaseModel):
    pass

class Courcse(BaseModel):
    pass

class Classes(BaseModel):
    pass


class Student(object):
    pass



