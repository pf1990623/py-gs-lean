#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: ftp_server.py
@time: 2018/12/28 11:17
"""
import os
import hashlib
import socketserver
import json
import configparser
from conf import settings


STATUS_CODE = {
    100: "INVALID CMD formart e.g{'aciton':'get',filename:'test.py,size:3343}",
    101: "Invalid cmd",
    252: "invalid auth data ",
    253: "wrong username or password"
}

class FtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:    # 持续交互
            self.data = self.request.recv(1024).stript()
            print(self.client_address[0])
            print(self.data)
            if not self.data: break
            data = json.loads(self.data.decode)
            if data.get("action") is not None:
                if hasattr(self,"_%s" % data.getdata.get("action")):
                    func = getattr("_%s" % data.getdata.get("action"))
                    func(data)
                else:
                    print("invalid cmd")
            else:
                print("invalid cmd format")
                self.send_responce(100)

    def send_responce(self,status_code,data):
        """
        向客户端返回数据
        :param status_code:
        :param data:
        :return:
        """
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get("username") is None or data.get["password"] is None:
            self.send_responce(252)
        user = self.authenticate(data.get("username"),data.get["password"])
        if user is None:
            self.send_responce(253)
        else:
            print("pass authtidate ",user)


    def authenticate(self,username,passwpord):
        """验证用户合法性"""
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == passwpord:
                print("pass auth..,", username)
                return config[username]


    def _put(self, *args, **kwargs):
        """client send file to server"""
        pass

    def _get(self, *args, **kwargs):
        """server send file client"""
        pass

    def _ls(self,*args, **kwargs):
        pass

    def _cd(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 9000

"""
ftp server
put
get
ld
dir
mkdir
touch
mv  src dest
copy src dest
rm
"""