#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: pan feng
@license: Apache Licence 
@file: 抽象类.py
@time: 2018/12/21 17:27
"""
#
# import abc
# abc 为抽象类

class Alert(object):
    """
    报警基类
    """
    def send(self):
        """
        报警消息发送接口
        :return:
        """
        raise NotImplementedError


class MailAlert(Alert):
    def send(self, msg):
        print("send".center(30,'.'), msg)


class SmsAlert(Alert):
    pass


m = MailAlert()
m.send("dddd")
