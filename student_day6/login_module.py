#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: login_module.py
@time: 2018/11/29 16:19
"""
"""
很多程序都有记录日志需求，并且日志中包含的信息即有正常的程序访问日志，还可能有警告信息、错误等信息输出，python的loggin
模块，提供了标准的日志接口，你可以通过它存储各种格式日志，logging的日志可以分为debug(),info(),warning(),error()and
critical() 5个级别，下面是使用方法

"""
import logging

# logging.debug("test debug")
#
# logging.info("testinfo")
#
logging.warning("user [xiaofeng] attempted wrong [assword more than 3 times")
#
# logging.error("test error")
#
# logging.critical("server is down")

"""
默认是root用户，可以指定用户
WARNING:root:user [xiaofeng] attempted wrong [assword more than 3 times
CRITICAL:root:server is down


"""

#  输出到文件
# logging.basicConfig(filename="log.log", level=logging.warning("waring"))
logging.basicConfig(filename="log.log", level=logging.error("xxxx"))