#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: sock_servers.py
@time: 2018/12/27 14:51
"""
import socketserver
# s = socketserver.TCPServer
# s1 = socketserver.UDPServer
"""
Baseserver
\\\
\\\
Tcpserver ----- unixstream server
\\\
\\\
Udpserver-----uxix
必须定义一个类，继承baseRequestHandler

ForKingUDPServer 
ForKingUDPServer  
ThreadingTCPServer  # 支持TCP并发
ThreadingUCPServer

"""


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:    # 持续交互
            self.data = self.request.recv(1024).stript()
            print(self.client_address[0])
            print(self.data)
            self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9000
    # create eht server ,binding top localhost on port 90000
    # 创建服务地址和监听端口
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    # Activate the server ,thjis will keep running until you
    # interrrupt the progran with ctrl-C
    server.serve_forever()

"""
sockerserver  核心原理： 线程


"""