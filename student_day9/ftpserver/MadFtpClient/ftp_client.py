#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: ftp_client.py
@time: 2018/12/28 11:34
"""
import socket
import os,json
import optparse


class FtpClient(object):
    def __int__(self):
        parser = optparse.OptionParser
        parser.add_option("-s", "--server", dest="server", help= "ftp server ip")
        parser.add_option("-P", "--port",type=int,dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="ftp user")
        parser.add_option("-p", "--password", dest="password", help="ftp user password")
        self.options, self.args = parser.parse_args()
        self.verity_args(self.options, self.args)

    def verity_args(self, options, args):
        """校验参数的合法性"""
        if options.usname is None and options.password is None:
            print("xxxxx")
        else:
            if options.usname is None or options.password is None:
                print("Err: username and password ")
        if options.server and options.port:
            print(options)
            if options.port >0 and options.port <65535:
                return True
            else:
                exec("Err: host port must in ")

    def authenticate(self):
        if self.options.username:
            print(self.options.username,self.options.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = input("password").strip()
                self.get_auth_result(username,password)


    def interactive(self):
        if self.authenticate():
            print("xxxxx")



if __name__ == "__main__":
    ftp = FtpClient()
    ftp.interactive()