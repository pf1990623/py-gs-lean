#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 唯一字符串生成方式.py
@time: 2018/12/20 10:13
"""
import uuid
import hashlib
import time


def create_uuid():
    return str(uuid.uuid1())


def create_md5():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding="utf-8"))
    return m.hexdigest()


if __name__ == '__main__':
    print(create_uuid())
    print(create_uuid())
    print(create_uuid())
    print(create_md5())
