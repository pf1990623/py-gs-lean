#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: 抽象接口.py
@time: 2018/12/21 17:20
"""

import abc

class Alert(object):
    """
    报警基类
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send(self):
        """
        报警消息发送接口
        :return:
        """
        pass


class MailAlert(Alert):
    pass



m = MailAlert()
m.send()
