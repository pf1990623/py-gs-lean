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
import os
import json
import optparse
import getpass

STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd ",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
}


class FtpClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_addr")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-p", "--password", dest="password", help="password")
        self.options, self.args = parser.parse_args()
        self.verify_args(self.options, self.args)
        self.make_connection()


    def make_connection(self):
        """
        创建连接
        :return: 没有返回
        self.options.server服务端IP地址，
        self.options.port 服务端端口
        """
        self.sock = socket.socket()  # 客户端socker
        self.sock.connect((self.options.server, self.options.port))

    def verify_args(self, options, args):
        """
        校验参数合法性
        :param options:
        :param args:
        :return:
        """
        if options.username is not None and options.password is not None:
            # 判断username和password都不是空的情况
            pass
        elif options.username is None and options.password is None:
            # 判断username和password 都是空的情况
            pass
        else:
            # 如果都没有，退出
            exit("Err: username and password ")
        if options.server and options.port:
            # 判断服务地址和端口都存在的情况下
            if options.port > 0 and options.port <65535:
                # 判断端口范围，如果在0~65535返回True
                return True
            else:
                # 如果不在0~65535，返回端口超出范围
                exit("Err: host port must in ")

    def authenticate(self):
        """
        用户验证功能
        :return:
        """
        # print(self.options.username)
        if self.options.username:
            print(self.options.username, self.options.password)
            return self.get_auth_result(self.options.username, self.options.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = input("password").strip()
                self.get_auth_result(username, password)

    def get_auth_result(self, user, password):
        data = {"action": "auth",
                "username": user,
                "password": password
                }
        self.sock.send(json.dumps(data).encode())
        self.get_response()

    def get_response(self):
        """
        得到服务器回复结果
        :return:
        """
        data = self.sock.recv(1024)
        data = json.loads(data.decode())
        print("responce data:", data)

    def interactive(self):
        if self.authenticate():
            print("----start interactive iwth u...")
            while True:
                choise = input("[%s]:"%self.user).strip()
                if len(choise) ==0:continue
                cmd_list = choise.split()
                if hasattr(self,"_%s"%cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd")
    def __md5_required(self,cmd_list):
        """
        检验命令是否需要MD5验证
        :param cmd_list:
        :return:
        """
        if "--md5" in cmd_list:
            return True

if __name__ == "__main__":
    ftp = FtpClient()
    ftp.interactive()   # 交互
