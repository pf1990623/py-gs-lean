#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: hashlib_module.py
@time: 2018/11/29 15:22
"""
"""
省内存：一行一行进行md5加密
不省内存：一次性读取所有文件，然后进行md5加密
一般用sha256就可以
"""
import hashlib
hash = hashlib.md5()

hash.update(b"admin")
print(hash.hexdigest())

hash.update(b"xiao")
print(hash.hexdigest())

hash2 = hashlib.md5()
hash.update(b"adminxiao")
print(hash.hexdigest())

