#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: test.py
@time: 2018/12/26 10:02
"""

import subprocess
res = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)