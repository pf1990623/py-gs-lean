#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: hmac_module.py
@time: 2018/11/29 15:30
"""

import hmac
h = hmac.new(b"salt", b'hello')       # 网路的消息加密传输,貌似不支持中文
print(h.hexdigest())

"""
如何解析，后面介绍

"""