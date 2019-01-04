#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: test.py
@time: 2019/1/4 12:35
"""
import optparse

parser = optparse.OptionParser()
parser.add_option("-s", "--server", dest="server", help="ftp server ip")
parser.add_option("-P", "--port", type=int,dest="port", help="ftp server port")
parser.add_option("-u", "--username", dest="username", help="ftp user")
parser.add_option("-p", "--password", dest="password", help="ftp user password")
(options,args) = parser.parse_args()
# self.verify_args(self.options, self.args)
# self.make_connection()
print(options.server)
print(options.port)

