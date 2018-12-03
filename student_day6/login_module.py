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
# import logging
#
# # 日志写入到文件，应该先定义logging.baseConfig
# logging.basicConfig(filename='log.log',
#                     level=logging.WARNING,
#                     format='%(asctime)s %(message)s',   # 时间格式
#                     datefmt='%m/%d/%Y %I:%M:%S %p')     # 日期格式
#
# logging.debug("test debug")
#
# logging.info("testinfo")
#
# logging.warning("user [xiaofeng] attempted wrong [assword more than 3 times")
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
# logging.basicConfig(filename="log.log", level=logging.warning,)
# logging.basicConfig(filename="log.log", level=logging.error("xxxx"))

# 日志加时间
# logging.warning('is when this event was logged')

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
# 如果想同时把log打印在屏幕和日志文件里，就需要了解一点复杂的知识了
# python使用loggin模块记录日志涉及四个主要类，使用给官方文档概括最为合适：
"""
logger:提供了应用程序可以直接使用的接口
handle:将（logger创建的）日志记录发送到合适的目的地输出；
filter:提供了吸毒设备来决定输出哪条日志记录
formatter：决定了日志输出的最终格式


logger
    每个程序在输出信息之前都要获得一个Logger.Logger通常对应了程序的模块名，比如聊天工具的图像界面模块，
    可以这样获得它的Logger:
        log=loggin.getLogger("chat.gui")
    而核心模块可以这样：
        log=loggin.getLogger("chat.kernel")
        Logger.setLevel(“level”):指定最低的日志级别，低于level的级别将被忽略，dubug是最低的内置级别
            critical为最高级别
        Logger.addFilter(filter)、Logger.removeFilter(filter): 添加或删除指定的filter
        Logger.addHandler("handler")、Logger.removeHandler("handler"): 添加或删除指定的handler
        Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()： 可以设置日志级别
handler
    handler对象负责发送相关信息到指定的目的地。python的日志系统有很多handler可以使用，有些handler可以把信息输出到控制
    台，有些Logger可以把信息输出到文件，有些Handler可以把信息发送到网络上，如果觉得够用，还可以辨析自己的Handler，。
    可以通过addHandler()方法添加多个Handler
    Handler.setLevle(level): 指定被处理信息的信息级别，低于level级别的信息将被忽略
    Handler.setFormatter(): 给Handler选择一个格式
    Handler.addFIlter(filter)、Handler.removeFilter(filter): 新增或删除一个filger对象

每个Logger可以附加多个Handler,在此我们介绍几个常用的Handler:
    1) logging.SreamHandler
        使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象（file object）它的构造函数是：
            StreamHandler([sterm])
            strm参数是一个文件对象。默认是sys.stderr
            
    2) logging.FileHandler
        和StreamHandle类似，用于一个文件输出日志信息。不过FileHandler会帮你打开这个文件，它的构造函数是：
        FileHandler(filename[,mode])
        filename是文件名，必须指定一个文件名
        mode是文件的打开方式。参见Python内置函数open()的方法。默认是 a,即天机到文件末尾
    
    3）logging.handlers.RotatingFiileHandler
        这个Handler类似上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前
        日志文件改名，然后创建一个新的同名日志文件继续输出。比如 日志文件chat.log。当chat.log达到指定大小之后
        RotatingFileHandler自动把文件改为chat.log.1,不过，如果chat.log.1已经存在，会先把chat.log.1重命名
        为chat.log.2 ....最后重新创建char.log，继续输出日志信息。它的构造函数是：
        RotatingFileHandler(filename[,mode[, maxBytes[,backupcount]]])
        其中：
            filename：是文件名，必须指定一个文件名
            mode：是文件的打开方式。参见Python内置函数open()的方法。默认是 a,即天机到文件末尾
            maxBytes：用于指定日志文件的最大文件大小。如果maxBytes为0，意味着日志文件可以无线增大，这时上面描述
                的重名过过程则不会发生。
            backupCount: 用于指定保留的备份文件个个数，比如，如果指定为2，当上面描述的重命名过程发生时，原有的chat.log.2
                并不会被修改名字，而是被删除。
    4） logging.handlers.TimedRotatingFileHandler
        这个Handler和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建文件，而是间隔一定时间就会自动
        创建新的日志文件。重命名过程与RotatingFileHandler类似，不过新的文件不再是以数字结尾，而是以当前时间结尾。他的构造函数是“
        TimedRotatingFileHandler(filename[,when[,interval[backupCount]]])”
         其中：
            filename：是文件名，必须指定一个文件名
            mode：是文件的打开方式。参见Python内置函数open()的方法。默认是 a,即天机到文件末尾
            interval：是时间间隔
            when：参数是一个字符串，表示时间间隔的单位，不区分大小写，它有一下取值：
                S: 秒
                M：分
                H: 小时
                D: 天
                W：每星期（interval==0,表示代表星期一）
                midnight: 每天凌晨‘’
            
"""

# 示例 日志显示又在屏幕，又需要在文件同时输出
# import logging
#
# # create logger
# logger = logging.Logger("test.log")
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set log level to debug
# # 创建console 的handler 和设置 日志级别
#
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create file handler and set log level to warning
#
# fh = logging.FileHandler("access.log")
# fh.setLevel(logging.WARNING)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # Add formatter to ch an fh
#
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
#
# # Add ch and fh to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
#
# # application code
# logger.debug("test dubug")
# logger.info("test info")
# logger.warning("test warning")
# logger.error("test error")
# logger.critical("test critical")



# 示例2：日志文件截断

"""
日志文件阶段需要单独的handers模块


"""
import logging
from logging import handlers

logger = logging.getLogger("TEST")

log_file = "timelog.log"

fh = handlers.RotatingFileHandler(filename=log_file, maxBytes=10, backupCount=3)
# fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S", interval=5,backupCount=3)

formatter = logging.Formatter('%(asctime)s  %(module)s:%(lineno)d  %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)

logging.warning("test 1")
logging.warning("test 11")
logging.warning("test 12")
logging.warning("test 13")
logging.warning("test 14")
logging.warning("test 11")
logging.warning("test 12")
logging.warning("test 13")
logging.warning("test 14")
logging.warning("test 11")
logging.warning("test 12")
logging.warning("test 13")
logging.warning("test 14")


