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

# 日志写入到文件，应该先定义logging.baseConfig
logging.basicConfig(filename='log.log',
                    level=logging.WARNING,
                    format='%(asctime)s %(message)s',   # 时间格式
                    datefmt='%m/%d/%Y %I:%M:%S %p')     # 日期格式

logging.debug("test debug")

logging.info("testinfo")

logging.warning("user [xiaofeng] attempted wrong [assword more than 3 times")

logging.error("test error")

logging.critical("server is down")

"""
默认是root用户，可以指定用户
WARNING:root:user [xiaofeng] attempted wrong [assword more than 3 times
CRITICAL:root:server is down


"""

#  输出到文件
# logging.basicConfig(filename="log.log", level=logging.warning,)
# logging.basicConfig(filename="log.log", level=logging.error("xxxx"))

# 日志加时间
logging.warning('is when this event was logged')

"""
日志输出格式：
%(levelno)s             数字形式的日志级别
%(levelname)s           文本形式的日志级别
%(pathname)s            调用日志输出函数的模块的完整路径名，可能没有
%(filename)s            调用日志输出函数的模块的文件名
%(module)s              调用日志输出函数的模块名
%(funcName)s            调用日志输出函数的函数名
%(lineno)d              调用日志输出函数的语句所在的代码行
%(created)f             当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d     输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s             字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d              线程ID。可能没有
%(threadName)           s线程名。可能没有
%(process)d             进程ID。可能没有
%(message)s             用户输出的消息

"""


#  日志显示又在屏幕，又需要在文件同时输出
