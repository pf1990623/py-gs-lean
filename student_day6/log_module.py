#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: log_module.py
@time: 2018/11/30 9:30
"""
import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG)
logging.debug("test debug")
logging.info("test info")
logging.warning("test warnging")
logging.error("test error")
logging.critical("test critical")
