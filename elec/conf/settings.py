#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence
@file: settings.py
@time: 2018/12/20 14:16
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB_DIR = os.path.join(BASE_DIR, 'db', 'admin')
# print(ADMIN_DB_DIR)

SCHOOL_DB_DIR = os.path.join(BASE_DIR, 'db', 'school')

TEACHER_DB_DIR = os.path.join(BASE_DIR, 'db', 'teacher')

COURSE_DB_DIR = os.path.join(BASE_DIR, 'db', 'course')

CLASSES_DB_DIR = os.path.join(BASE_DIR, 'db', 'classes')

STUDENT_DB_DIR = os.path.join(BASE_DIR, 'db', 'student')

COURSE_TO_TEACHER_DB_DIR = os.path.join(BASE_DIR, 'db', 'course_to_teacher')

if __name__ == "__main__":
    print(ADMIN_DB_DIR)
    print(SCHOOL_DB_DIR)
    print(TEACHER_DB_DIR)
    print(COURSE_DB_DIR)
    print(CLASSES_DB_DIR)
    print(STUDENT_DB_DIR)
    print(COURSE_TO_TEACHER_DB_DIR)
    print(BASE_DIR)
