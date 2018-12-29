#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: main.py
@time: 2018/12/27 16:44
"""

import optparse
from core.ftp_server import Ftphandler
import socketserver
from conf import settings
"""
参数处理模块
"""
class ArgvHandler(object):
    def __init__(self):
        self.parse = optparse.OptionParser()
        # parse.add_option("-s","--host",dest="host",help="server listen binding host address")
        # parse.add_option("-p", "--port", dest="host port", help="server listen binding port")
        (options,args) = self.parse.parse_args()
        self.verify(options,args)


    def verify_args(self,options,args):
        """
        校验并调用相应的功能
        :param options:
        :param args:
        :return:
        """
        if hasattr(self,args[0]):
            func = getattr(self.args[0])
            func()
        else:
            self.parse.print_help()


    def start(self):
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), Ftphandler)
        server.serve_forever()



