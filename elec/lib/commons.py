#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: commons.py
@time: 2018/12/20 14:11
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
    print(create_md5())
    print(create_uuid())