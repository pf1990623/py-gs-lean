#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: ftp_server.py
@time: 2018/12/28 11:17
"""

import socketserver
import json

class FtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:    # 持续交互
            self.data = self.request.recv(1024).stript()
            print(self.client_address[0])
            print(self.data)
            data = json.loads(self.data)
            if data.get("action") is not None:
                if hasattr(self,"__%s" % data.getdata.get("action")):
                    func = getattr("__%s" %data.getdata.get("action"))
                    func(data)
            else:
                print("invalid cmd")
    def __put(self,*args,**kwargs):
        """client send file to server"""
        pass

    def __get(self,*args,**kwargs):
        """server send file client"""
        pass

    def __ls(self,*args,**kwargs):
        pass

    def __cd(self,*args,**kwargs):
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