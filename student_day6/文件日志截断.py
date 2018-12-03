#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 文件日志截断.py
@time: 2018/12/3 17:50
"""
import logging

from logging import handlers

logger = logging.getLogger(__name__)

log_file = "timelog.log"
# 根据文件指定大小切割
# fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3)

fh = handlers.TimedRotatingFileHandler(filename=log_file, encoding='utf8', when="S",interval=5, backupCount=3)


formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)


logger.warning("test1")
logger.warning("test12")
logger.warning("test13")
logger.warning("test14")
logger.warning("test1")
logger.warning("test12")
logger.warning("test13")
logger.warning("test14")