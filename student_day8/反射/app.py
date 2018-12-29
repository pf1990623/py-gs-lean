#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: app.py
@time: 2018/12/25 10:22
"""

from controller import account

action = input(">>>").strip()

if (hasattr(account, action)):
    func = getattr(account,action)
    result = func()
else:
    result = "404"

print(result)
